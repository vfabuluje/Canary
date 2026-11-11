-- SVB (cert 24735) at 2022-12-31: HTM unrealized loss / equity is about 0.98 (15.2B loss on 15.5B equity).
-- Returns a row if the bank-quarter is missing or the value is outside 0.90-1.05.
select cert, report_date, htm_unrealized_loss_to_equity
from {{ ref('fct_bank_features') }}
where cert = 24735 and report_date = date '2022-12-31'
  and (htm_unrealized_loss_to_equity is null
       or htm_unrealized_loss_to_equity not between 0.90 and 1.05)
union all
select 24735, date '2022-12-31', cast(null as double)
where not exists (
    select 1 from {{ ref('fct_bank_features') }}
    where cert = 24735 and report_date = date '2022-12-31')
