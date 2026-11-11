-- 31 CAMELS-style features per bank per quarter. Keys + features only: no label, name or failure columns.
-- FDIC ratio fields pass through in percent; ratios computed here are fractions.
-- Every denominator is wrapped in nullif(x, 0) so division by zero gives null, not an error.
-- See decisions/0009-features-and-zero-handling.md.
with base as (
    select
        *,
        -- Year-to-date dollars become annualized: x 4 / quarter number (Q1 x4, Q2 x2, Q3 x4/3, Q4 x1)
        cast(4 as double) / quarter(report_date) as ytd_to_annual,
        -- 0 means "not reported" for these (decision 0009)
        nullif(tier1_risk_based_ratio, 0) as tier1_clean,
        nullif(total_risk_based_ratio, 0) as total_rbc_clean,
        nullif(uninsured_deposits, 0) as uninsured_clean
    from {{ ref('fct_bank_quarters') }}
),

prior as (
    -- Same bank's row exactly 12 months earlier, matched on date (not row position).
    select cert, report_date, total_assets, total_deposits
    from {{ ref('fct_bank_quarters') }}
)

select
    b.cert,
    b.report_date,

    -- Capital (FDIC ratios, percent)
    b.equity_to_assets_ratio as equity_to_assets,
    b.leverage_ratio,
    b.tier1_clean as tier1_risk_based_ratio,
    b.total_rbc_clean as total_risk_based_ratio,

    -- Asset quality (fractions)
    b.noncurrent_loans / nullif(b.gross_loans_and_leases, 0) as noncurrent_loans_to_loans,
    (b.nonaccrual_assets + b.other_real_estate_owned) / nullif(b.total_assets, 0) as nonaccrual_ore_to_assets,
    b.past_due_30_89_assets / nullif(b.total_assets, 0) as past_due_30_89_to_assets,
    b.loan_loss_allowance / nullif(b.gross_loans_and_leases, 0) as allowance_to_loans,
    (b.net_charge_offs * b.ytd_to_annual) / nullif(b.gross_loans_and_leases, 0) as net_charge_offs_to_loans_ann,
    (b.provision_for_credit_losses * b.ytd_to_annual) / nullif(b.total_assets, 0) as provision_to_assets_ann,
    b.construction_land_loans / nullif(b.gross_loans_and_leases, 0) as construction_loans_to_loans,
    b.commercial_real_estate_loans / nullif(b.gross_loans_and_leases, 0) as cre_loans_to_loans,
    (b.noncurrent_loans + b.other_real_estate_owned)
        / nullif(b.equity_capital + b.loan_loss_allowance, 0) as texas_ratio,

    -- Earnings (FDIC ratios, percent, except the computed _ann fraction)
    b.return_on_assets,
    b.return_on_equity,
    b.net_interest_margin,
    b.efficiency_ratio,
    (b.total_interest_expense * b.ytd_to_annual) / nullif(b.total_assets, 0) as interest_expense_to_assets_ann,

    -- Liquidity
    b.net_loans_to_deposits_ratio as loans_to_deposits,
    b.uninsured_clean / nullif(b.total_deposits, 0) as uninsured_to_deposits,
    b.brokered_deposits / nullif(b.total_deposits, 0) as brokered_to_deposits,
    b.core_deposits / nullif(b.total_assets, 0) as core_deposits_to_assets,
    b.fhlb_advances / nullif(b.total_assets, 0) as fhlb_to_assets,
    b.volatile_liabilities / nullif(b.total_assets, 0) as volatile_liabilities_to_assets,
    b.cash_and_due_from_banks / nullif(b.total_assets, 0) as cash_to_assets,

    -- Sensitivity: 0 if no bonds in the bucket; null if cost > 0 but fair value is 0 or missing
    case
        when b.htm_securities_amortized_cost = 0 then 0.0
        when b.htm_securities_fair_value is null or b.htm_securities_fair_value = 0 then null
        else (b.htm_securities_amortized_cost - b.htm_securities_fair_value) / nullif(b.equity_capital, 0)
    end as htm_unrealized_loss_to_equity,
    case
        when b.afs_securities_amortized_cost = 0 then 0.0
        when b.afs_securities_fair_value is null or b.afs_securities_fair_value = 0 then null
        else (b.afs_securities_amortized_cost - b.afs_securities_fair_value) / nullif(b.equity_capital, 0)
    end as afs_unrealized_loss_to_equity,
    b.total_securities / nullif(b.total_assets, 0) as securities_to_assets,

    -- Size and growth (growth looks backward only)
    case when b.total_assets > 0 then ln(b.total_assets) end as log_total_assets,
    b.total_assets / nullif(p.total_assets, 0) - 1 as asset_growth_4q,
    b.total_deposits / nullif(p.total_deposits, 0) - 1 as deposit_growth_4q
from base as b
left join prior as p
    on b.cert = p.cert
    and p.report_date = date_add('month', -12, b.report_date)
