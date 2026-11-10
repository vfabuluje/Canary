-- Every quarter should have 3,000-12,000 banks. Returns quarters outside that range.
select report_date, count(*) as n_rows
from {{ ref('stg_fdic__financials') }}
group by report_date
having count(*) < 3000 or count(*) > 12000
