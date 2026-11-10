-- SVB failed 2023-03-10 (Q1 2023), so its 2022-12-31 row must be 1 quarter before failure. Returns a row if not.
select cert, report_date, quarters_until_failure
from {{ ref('fct_bank_quarters') }}
where cert = 24735 and report_date = date '2022-12-31'
  and (quarters_until_failure is null or quarters_until_failure <> 1)
