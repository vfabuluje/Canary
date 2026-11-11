-- Growth features must be null when the bank has no row exactly 12 months earlier. Returns offending rows.
select f.cert, f.report_date, f.asset_growth_4q, f.deposit_growth_4q
from {{ ref('fct_bank_features') }} as f
where (f.asset_growth_4q is not null or f.deposit_growth_4q is not null)
  and not exists (
    select 1 from {{ ref('fct_bank_quarters') }} as p
    where p.cert = f.cert and p.report_date = date_add('month', -12, f.report_date))
