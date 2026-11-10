select
    f.*,
    d.failure_date,
    case
        when d.failure_date is null then null
        else cast(
            (year(d.failure_date) * 4 + quarter(d.failure_date))
            - (year(f.report_date) * 4 + quarter(f.report_date))
            as integer)
    end as quarters_until_failure
from {{ ref('stg_fdic__financials') }} as f
left join {{ ref('dim_failed_banks') }} as d
    on f.cert = d.cert
