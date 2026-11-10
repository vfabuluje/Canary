# Runbook: AWS setup (one time)

Creates the S3 bucket, Glue databases, Athena workgroup, cost budget and the limited `canary-dev` user. Why each choice: [[decisions/0008-aws-setup-and-cost-guardrails]]. Spec: [[specs/2026-11-09-phase2-warehouse-design]].

Everything is in region **us-east-1** (N. Virginia). Total cost should stay under $5/month.

## (a) Secure the root account
1. Sign in at https://console.aws.amazon.com as the root user (the email you signed up with).
2. Account menu > Security credentials > **Assign MFA device** and follow the steps with an authenticator app.
   - Why: root can do anything and cannot be limited. MFA means a stolen password alone is not enough.

## (b) Make an admin user, then stop using root
1. IAM > Users > Create user. If the console asks, choose "I want to create an IAM user" (not Identity Center). Name it e.g. `admin`, tick "Provide user access to the AWS Management Console", set a password.
2. Attach the AWS managed policy `AdministratorAccess`.
3. Open that user > Security credentials > **Assign MFA device**.
4. Still as root, open Account (top right menu) > find "IAM user and role access to Billing information" > **Edit > Activate**. Without this, the admin user cannot create the budget in step (c) and the script fails.
5. Sign out of root. From now on sign in with the admin user (use the account sign-in URL shown on the IAM dashboard).
   - Why: day-to-day work should never use root.

## (c) Run the setup script in CloudShell
CloudShell is a terminal inside the AWS console that is already logged in as you, so no keys are needed on your Mac.
1. Signed in as admin, make sure the region (top right) is **N. Virginia (us-east-1)**, then click the CloudShell icon.
2. Upload `infra/setup.sh` and `infra/iam-policy-canary-dev.json` (Actions > Upload file). Both must land in the same folder.
3. Pick a bucket name: `canary-warehouse-` plus 6 random lowercase letters/digits, e.g. `canary-warehouse-k3x9qa`. Bucket names are global, so random letters avoid clashes.
4. Run:
```
CANARY_BUCKET=canary-warehouse-k3x9qa ALERT_EMAIL=you@example.com bash setup.sh
```
   - `CANARY_BUCKET=... ALERT_EMAIL=...` hands the two values to the script for this one run only. They are never saved in the repo.
   - `bash setup.sh` runs the script. It prints a numbered step for each resource and skips anything that already exists, so it is safe to run again.

What the script does, in order: creates the bucket; blocks all public access; turns on encryption; deletes `athena-results/` files after 7 days; creates databases `canary_raw`, `canary_staging`, `canary_marts`; creates the Athena workgroup `canary` (1 GB scan limit per query); creates a $5/month budget with email alerts; creates the `canary-dev` user with the limited policy.

## (d) Confirm the budget email
AWS emails `ALERT_EMAIL` about the budget. Check inbox/spam and click the confirmation link if one arrives. Alerts fire at 50% and 100% of $5 spent, and when AWS forecasts you will pass $5.

## (e) Create an access key for canary-dev
1. IAM > Users > `canary-dev` > Security credentials > **Create access key**.
2. Choose "Command Line Interface (CLI)", create it, and copy the Access key ID and Secret access key (the secret is shown once).
   - The script does not do this for you on purpose: a secret key should never appear in a script or a log.

## (f) Configure your Mac
```
brew install awscli
```
Installs the AWS command line tool.
```
aws configure --profile canary
```
Saves the key under a named profile `canary`. Paste the key ID and secret, region `us-east-1`, output format `json`. The keys go into `~/.aws/`, outside the repo.
```
cp .env.example .env
```
Then edit `.env` and set `CANARY_BUCKET` to your real bucket name. `.env` is git-ignored; never commit it.

## (g) Check it works
```
aws sts get-caller-identity --profile canary
```
Asks AWS "who am I with this profile?". The `Arn` should end in `user/canary-dev`. If it shows anything else, stop and fix the profile.

## Revoke access
IAM > Users > `canary-dev` > Security credentials > access key > **Deactivate**, then **Delete**. The Mac profile stops working immediately. Then remove the `[canary]` section from your `~/.aws/credentials` and `~/.aws/config` yourself (open them in your own editor; nothing in this project or Claude should read those files). Create a new key with step (e) to restore access.

## If something goes wrong
- `BucketAlreadyExists`: someone else owns that name; pick new random letters.
- `AccessDenied` in CloudShell: you are not signed in as the admin user.
- Re-running the script is always safe.
