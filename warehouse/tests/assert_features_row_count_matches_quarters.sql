-- fct_bank_features must have exactly one row per fct_bank_quarters row. Returns a row if the counts differ.
select f.n as feature_rows, q.n as quarter_rows
from (select count(*) as n from {{ ref('fct_bank_features') }}) as f
cross join (select count(*) as n from {{ ref('fct_bank_quarters') }}) as q
where f.n <> q.n
