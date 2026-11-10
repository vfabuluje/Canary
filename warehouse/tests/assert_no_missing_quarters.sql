-- Returns each expected quarter-end (2001-03-31 .. latest report_date) with no rows. Any row = failure.
with bounds as (select max(report_date) as max_date from {{ ref('stg_fdic__financials') }}),
expected as (
    select last_day_of_month(q) as report_date
    from bounds
    cross join unnest(sequence(date '2001-03-31', bounds.max_date, interval '3' month)) as t(q)
),
actual as (select distinct report_date from {{ ref('stg_fdic__financials') }})
select expected.report_date
from expected
left join actual on expected.report_date = actual.report_date
where actual.report_date is null
