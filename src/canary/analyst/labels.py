"""Plain-English names, units and display forms for the 31 model features.

Units follow data-dictionary/fct_bank_features.md: "pct" columns are already in percent
(8.5 = 8.5%), "frac" columns are fractions (0.085 = 8.5%), and log_total_assets is the
natural log of total assets in thousands of dollars.
"""

import math

PLAIN_NAMES: dict[str, str] = {
    "equity_to_assets": "equity as a share of assets",
    "leverage_ratio": "the leverage ratio (core capital as a share of average assets)",
    "tier1_risk_based_ratio": "the Tier 1 risk-based capital ratio",
    "total_risk_based_ratio": "the total risk-based capital ratio",
    "noncurrent_loans_to_loans": "loans 90+ days past due or not accruing interest, as a share of loans",
    "nonaccrual_ore_to_assets": "nonaccrual assets and foreclosed property, as a share of assets",
    "past_due_30_89_to_assets": "loans 30-89 days past due, as a share of assets",
    "allowance_to_loans": "loan-loss reserves as a share of loans",
    "net_charge_offs_to_loans_ann": "annualized loan write-offs, net of recoveries, as a share of loans",
    "provision_to_assets_ann": "annualized provision for loan losses as a share of assets",
    "construction_loans_to_loans": "construction loans as a share of loans",
    "cre_loans_to_loans": "commercial real estate loans as a share of loans",
    "texas_ratio": "the Texas ratio (troubled assets against capital plus reserves)",
    "return_on_assets": "return on assets (profit as a share of assets)",
    "return_on_equity": "return on equity (profit as a share of equity)",
    "net_interest_margin": "net interest margin (the spread earned on lending and investing)",
    "efficiency_ratio": "the efficiency ratio (operating costs as a share of revenue)",
    "interest_expense_to_assets_ann": "annualized interest expense as a share of assets",
    "loans_to_deposits": "loans as a share of deposits",
    "uninsured_to_deposits": "uninsured deposits as a share of deposits",
    "brokered_to_deposits": "brokered deposits as a share of deposits",
    "core_deposits_to_assets": "core deposits as a share of assets",
    "fhlb_to_assets": "Federal Home Loan Bank borrowings as a share of assets",
    "volatile_liabilities_to_assets": "volatile funding as a share of assets",
    "cash_to_assets": "cash as a share of assets",
    "htm_unrealized_loss_to_equity": "losses on bonds held to maturity, as a share of equity",
    "afs_unrealized_loss_to_equity": "losses on bonds available for sale, as a share of equity",
    "securities_to_assets": "securities as a share of assets",
    "log_total_assets": "total assets",
    "asset_growth_4q": "asset growth over the past four quarters",
    "deposit_growth_4q": "deposit growth over the past four quarters",
}

_PCT = (
    "equity_to_assets",
    "leverage_ratio",
    "tier1_risk_based_ratio",
    "total_risk_based_ratio",
    "return_on_assets",
    "return_on_equity",
    "net_interest_margin",
    "efficiency_ratio",
    "loans_to_deposits",
)

UNIT: dict[str, str] = {
    name: "pct" if name in _PCT else "assets" if name == "log_total_assets" else "frac"
    for name in PLAIN_NAMES
}


def _assets_forms(log_assets: float) -> list[str]:
    dollars = math.exp(log_assets) * 1000  # the column is ln(assets in $ thousands)
    if dollars >= 1e9:
        return [f"${dollars / 1e9:.1f} billion", f"${dollars / 1e9:.0f} billion"]
    return [f"${dollars / 1e6:.1f} million", f"${dollars / 1e6:.0f} million"]


def display_forms(feature: str, value: float) -> list[str]:
    """Every accepted way to write `value`; the first is the one the analyst should print."""
    unit = UNIT[feature]
    if unit == "assets":
        return _assets_forms(value)
    percent = value if unit == "pct" else value * 100
    return [f"{percent:.1f}%", f"{percent:.0f}%", f"{value:.2f}"]
