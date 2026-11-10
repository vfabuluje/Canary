-- SVB, Signature and First Republic must be in dim_failed_banks with the right failure dates. Returns the ones that are wrong or missing.
with expected (cert, failure_date) as (
    values (24735, date '2023-03-10'), (57053, date '2023-03-12'), (59017, date '2023-05-01')
)
select e.cert, e.failure_date as expected_date, d.failure_date as actual_date
from expected e
left join {{ ref('dim_failed_banks') }} d on e.cert = d.cert
where d.failure_date is null or d.failure_date <> e.failure_date
