#!/usr/bin/env bash
# One-time AWS setup for Canary. Run in AWS CloudShell as an admin user.
#   CANARY_BUCKET=canary-warehouse-abc123 ALERT_EMAIL=you@example.com bash setup.sh
# Needs infra/iam-policy-canary-dev.json in the same folder as this script.
# Safe to re-run: every step skips with a message if the resource already exists.
# It does NOT create access keys for canary-dev; do that by hand in the console.
set -euo pipefail

: "${CANARY_BUCKET:?Set CANARY_BUCKET, e.g. canary-warehouse-abc123}"
: "${ALERT_EMAIL:?Set ALERT_EMAIL to the address for budget alerts}"

REGION="us-east-1"
USER_NAME="canary-dev"
POLICY_NAME="canary-dev-least-privilege"
POLICY_FILE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/iam-policy-canary-dev.json"
ACCOUNT_ID="$(aws sts get-caller-identity --query Account --output text)"

echo "== 1. S3 bucket"
if aws s3api head-bucket --bucket "$CANARY_BUCKET" 2>/dev/null; then
  echo "Bucket $CANARY_BUCKET already exists, skipping create."
else
  # us-east-1 is the one region where no LocationConstraint is allowed.
  aws s3api create-bucket --bucket "$CANARY_BUCKET" --region "$REGION"
fi

echo "== 2. Block all public access"
aws s3api put-public-access-block --bucket "$CANARY_BUCKET" \
  --public-access-block-configuration \
  BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true

echo "== 3. Default encryption (SSE-S3)"
aws s3api put-bucket-encryption --bucket "$CANARY_BUCKET" \
  --server-side-encryption-configuration \
  '{"Rules":[{"ApplyServerSideEncryptionByDefault":{"SSEAlgorithm":"AES256"}}]}'

echo "== 4. Lifecycle: delete athena-results/ after 7 days"
aws s3api put-bucket-lifecycle-configuration --bucket "$CANARY_BUCKET" \
  --lifecycle-configuration '{"Rules":[{"ID":"expire-athena-results","Status":"Enabled","Filter":{"Prefix":"athena-results/"},"Expiration":{"Days":7}}]}'

echo "== 5. Glue databases"
for db in canary_raw canary_staging canary_marts; do
  if aws glue get-database --name "$db" --region "$REGION" >/dev/null 2>&1; then
    echo "Glue database $db already exists, skipping."
  else
    aws glue create-database --database-input "{\"Name\":\"$db\"}" --region "$REGION"
  fi
done

echo "== 6. Athena workgroup 'canary'"
if aws athena get-work-group --work-group canary --region "$REGION" >/dev/null 2>&1; then
  echo "Workgroup canary already exists, skipping."
else
  aws athena create-work-group --name canary --region "$REGION" \
    --configuration "EnforceWorkGroupConfiguration=true,BytesScannedCutoffPerQuery=1073741824,EngineVersion={SelectedEngineVersion='Athena engine version 3'},ResultConfiguration={OutputLocation=s3://$CANARY_BUCKET/athena-results/}"
fi

echo "== 7. \$5 monthly cost budget"
if aws budgets describe-budget --account-id "$ACCOUNT_ID" --budget-name canary-monthly >/dev/null 2>&1; then
  echo "Budget canary-monthly already exists, skipping."
else
  notification() { # $1 = threshold percent, $2 = ACTUAL or FORECASTED
    echo "{\"Notification\":{\"NotificationType\":\"$2\",\"ComparisonOperator\":\"GREATER_THAN\",\"Threshold\":$1,\"ThresholdType\":\"PERCENTAGE\"},\"Subscribers\":[{\"SubscriptionType\":\"EMAIL\",\"Address\":\"$ALERT_EMAIL\"}]}"
  }
  aws budgets create-budget --account-id "$ACCOUNT_ID" \
    --budget '{"BudgetName":"canary-monthly","BudgetLimit":{"Amount":"5","Unit":"USD"},"TimeUnit":"MONTHLY","BudgetType":"COST"}' \
    --notifications-with-subscribers \
    "$(notification 50 ACTUAL)" "$(notification 100 ACTUAL)" "$(notification 100 FORECASTED)"
fi

echo "== 8. IAM user $USER_NAME with least-privilege policy"
if aws iam get-user --user-name "$USER_NAME" >/dev/null 2>&1; then
  echo "User $USER_NAME already exists, skipping create."
else
  aws iam create-user --user-name "$USER_NAME"
fi
# put-user-policy overwrites, so re-running also refreshes the policy.
POLICY_JSON="$(sed "s/BUCKET_NAME/$CANARY_BUCKET/g" "$POLICY_FILE")"
aws iam put-user-policy --user-name "$USER_NAME" --policy-name "$POLICY_NAME" \
  --policy-document "$POLICY_JSON"

echo "Done. Next: create ONE access key for $USER_NAME in the IAM console (see runbooks/aws-setup.md)."
