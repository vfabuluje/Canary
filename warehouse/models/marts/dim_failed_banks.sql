select
    cert,
    institution_name,
    failure_date,
    estimated_loss,
    total_assets_at_failure
from {{ ref('stg_fdic__failures') }}
where is_failure
  and failure_year >= 2001
  and cert is not null
