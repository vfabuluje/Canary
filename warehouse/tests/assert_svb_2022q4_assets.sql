-- SVB (cert 24735) at 2022-12-31 must report total assets of $209,026,000 thousand. Returns a row if not.
select cert, report_date, total_assets
from {{ ref('fct_bank_quarters') }}
where cert = 24735 and report_date = date '2022-12-31'
  and total_assets <> 209026000
union all
select 24735, date '2022-12-31', cast(null as bigint)
where not exists (
    select 1 from {{ ref('fct_bank_quarters') }}
    where cert = 24735 and report_date = date '2022-12-31')
