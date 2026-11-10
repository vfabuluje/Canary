-- Staging must not drop or add rows. Returns a row (= test fails) if the counts differ.
with staged as (select count(*) as n from {{ ref('stg_fdic__financials') }}),
raw as (select count(*) as n from {{ source('canary_raw', 'fdic_financials') }})
select staged.n as staged_rows, raw.n as raw_rows
from staged cross join raw
where staged.n <> raw.n
