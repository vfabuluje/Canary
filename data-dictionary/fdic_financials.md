# fdic_financials

Quarterly financial snapshot of every FDIC-insured bank, as published by the FDIC.

| | |
|---|---|
| Grain | One row per bank (`CERT`) per quarter (`REPDTE`) |
| Primary key | (`CERT`, `REPDTE`) |
| Source | `GET https://api.fdic.gov/banks/financials` (FDIC BankFind) |
| File | `data/raw/financials/repdte=YYYYMMDD/part.parquet` (one file per quarter) |
| Rows | 710,691 (102 quarters, 2001-03-31 to 2026-06-30; 9,940 rows in 2001-03-31 down to 4,313 in 2026-06-30) |

Design and reasoning: [[specs/2026-11-09-phase1-fdic-ingestion-design]]. Column names are FDIC's own, kept as-is so each can be looked up in FDIC docs. Values are stored exactly as published; the only conversion is blank to null.

## Read this before using the data

- **Dollar amounts are in thousands of dollars.** SVB's `ASSET` of 209,026,000 means $209 billion.
- **Ratios are percent.** An `RBC1AAJ` of 7.96 means a 7.96% leverage ratio, not 0.0796. A typical `ROA` is about 1.
- **Income fields are year-to-date.** Q4 covers the whole year, Q1 covers one quarter. This applies to the dollar fields `NETINC`, `EINTEXP`, `ELNATR` and `NTLNLS`; Phase 3 must convert them to per-quarter values. `ROA`, `ROE` and `NIMY` are annualized year-to-date ratios and are already comparable across quarters. `EEFFR` is a ratio of two year-to-date amounts (not annualized); no conversion needed.
- **0 can mean "not reported".** Some fields did not exist in early years (SVB's `SCHF` is 0 in 2001). Phase 1 keeps the 0; Phase 3 decides how to treat it.
- **Current, amended values only.** The API serves the latest corrected numbers for every quarter, not what the bank originally filed. A replay of SVB therefore uses numbers as corrected later, not exactly what an analyst saw in early 2023.
- **Blank is stored as null**, not as an empty string.

## Columns

| Column | Type | FDIC title | Meaning (plain English) | Units / caveats |
|---|---|---|---|---|
| `CERT` | int64 | FDIC Certificate # | The bank's unique FDIC ID number; the key for joining to the failures table. | Never null here. |
| `REPDTE` | date | Report Date | The quarter-end date this snapshot describes. | Stored as a timestamp at midnight (no time part), e.g. 2022-12-31 00:00. |
| `NAME` | string | INSTITUTION NAME | The bank's legal name. | Names can change over time. |
| `STALP` | string | FIPS STATE ALPHA CODE | Two-letter state where the bank is based. | |
| `BKCLASS` | string | INSTITUTION CLASS | Charter class: type of bank charter and who supervises it. | FDIC class code. |
| `NAMEHCR` | string | Bank Holding Company (Regulatory Top Holder) | Name of the parent holding company at the top of the ownership chain, if any. | Null for banks with no holding company. |
| `ASSET` | float64 | Total assets | Everything the bank owns: loans, securities, cash, and so on. The standard measure of a bank's size. | $ thousands. |
| `LIAB` | float64 | TOTAL LIABILITIES | Everything the bank owes: deposits, borrowings, and other debts. | $ thousands. |
| `DEP` | float64 | Total deposits | Money customers have placed in the bank. Deposits are the bank's main funding, and a run drains them. | $ thousands. |
| `EQ` | float64 | Equity capital | The cushion left after liabilities are subtracted from assets; it absorbs losses before depositors are hurt. | $ thousands. |
| `LNLSGR` | float64 | LOANS AND LEASES-TOTAL | Total loans and leases the bank has made, before setting aside reserves for losses. | $ thousands. |
| `SC` | float64 | SECURITIES | Total bonds and other securities the bank holds. Large holdings of long-term bonds lose value when interest rates rise, as at SVB. | $ thousands. |
| `RBC1AAJ` | float64 | LEVERAGE RATIO-PCA | Core capital as a share of average assets, a plain measure of how thick the loss cushion is. Regulators use it to judge whether a bank is adequately capitalized. | Percent. |
| `IDT1RWAJR` | float64 | TIER 1 RISK-BASED CAPITAL RATIO | Core capital as a share of risk-weighted assets (riskier assets count for more). | Percent. May be null or 0 in early years. |
| `RBCRWAJ` | float64 | TOTAL RBC RATIO-PCA | Total regulatory capital as a share of risk-weighted assets; the broadest capital ratio. | Percent. |
| `EQV` | float64 | BANK EQUITY CAPITAL/ASSETS | Equity as a share of total assets: how much of the bank is funded by owners rather than debt. | Percent. |
| `NCLNLS` | float64 | TOTAL N/C-LOANS & LEASES | Noncurrent loans: loans 90+ days past due or no longer accruing interest. A key sign of loans going bad. | $ thousands. |
| `NAASSET` | float64 | NONACCRUAL-TOTAL ASSETS | Assets (mostly loans) on which the bank has stopped counting interest income because repayment is doubtful. | $ thousands. |
| `P3ASSET` | float64 | 30-89 DAYS P/D-TOTAL ASSETS | Assets whose payments are 30 to 89 days late but still accruing interest: an early sign of borrower trouble. Separate from `NAASSET`. | $ thousands. Still-accruing only, so don't add to `NAASSET`/`NCLNLS` (noncurrent = 90+ days past due plus nonaccrual). |
| `P9ASSET` | float64 | 90+ DAYS P/D-TOTAL ASSETS | Assets whose payments are 90 or more days late but still accruing interest. Separate from `NAASSET`; noncurrent (`NCLNLS`) is this plus nonaccrual. | $ thousands. Still-accruing only; with `NAASSET` it roughly makes up `NCLNLS`, so don't count both. |
| `ORE` | float64 | OTHER REAL ESTATE OWNED | Property the bank has taken over after borrowers defaulted (foreclosed real estate). | $ thousands. |
| `LNATRES` | float64 | ALLOW FOR LOANS LOSS ADJUSTED | The reserve the bank has set aside to cover expected loan losses. Since CECL (2020 onward) it covers expected credit losses more broadly, not only incurred losses. | $ thousands. |
| `NTLNLS` | float64 | TOTAL LN&LS NET CHARGE-OFFS | Loans written off as uncollectible, minus later recoveries. | $ thousands. Year-to-date. |
| `ELNATR` | float64 | PROVISIONS FOR CREDIT LOSSES | Money the bank charged against earnings to add to its credit-loss reserve. Since CECL (2020 onward) it covers expected credit losses more broadly. | $ thousands. Year-to-date. |
| `LNRE` | float64 | RE LOANS | Loans secured by real estate. | $ thousands. |
| `LNRECONS` | float64 | RE CONSTRUCTION & LAND DEVELOP | Loans for building projects and land development, historically a risky category. | $ thousands. |
| `LNRENRES` | float64 | RE NONFARM NONRESIDENTIAL PROP | Commercial real estate loans (office buildings, shops, and similar, not homes or farms). | $ thousands. |
| `LNCI` | float64 | C&I LOANS | Commercial and industrial loans: loans to businesses for their operations. | $ thousands. |
| `NETINC` | float64 | Net income | Profit after all expenses and taxes. | $ thousands. Year-to-date. |
| `ROA` | float64 | Return on assets (ROA) | Profit as a share of assets: how efficiently the bank earns money. | Percent. Annualized, year-to-date: comparable across quarters without conversion. |
| `ROE` | float64 | Return on Equity (ROE) | Profit as a share of owners' equity. | Percent. Annualized, year-to-date: comparable across quarters without conversion. |
| `NIMY` | float64 | NET INTEREST MARGIN | Interest earned on loans and securities minus interest paid on deposits and borrowings, as a share of earning assets. A squeezed margin hurts profits. | Percent. Annualized, year-to-date: comparable across quarters without conversion. |
| `EINTEXP` | float64 | TOTAL INTEREST EXPENSE | Total interest the bank paid on deposits and borrowings. | $ thousands. Year-to-date. |
| `EEFFR` | float64 | EFFICIENCY RATIO | Operating costs per dollar of revenue; lower means the bank spends less to earn each dollar. | Percent. Ratio of two year-to-date amounts; not annualized, no conversion needed. |
| `DEPUNINS` | float64 | ESTIMATED UNINSURED DEPOSITS IN DOMESTIC OFFICES AND IN INSURED BRANCHES IN US TERRITORIES AND POSSESSIONS | Estimated deposits above the federal insurance limit, which customers have the most reason to pull in a panic (as at SVB). | $ thousands. An estimate, mainly reported by banks with $1B+ in assets, so often 0 or null for smaller banks and in early years. The limit was $100K until October 2008, then $250K (temporary, made permanent in 2010). |
| `BRO` | float64 | BROKERED DEP | Deposits the bank obtained through brokers rather than directly from customers; often more rate-sensitive and quicker to leave. | $ thousands. |
| `COREDEP` | float64 | CORE DEPOSITS | Stable deposits: broadly, total deposits minus large time deposits and brokered deposits. Generally less likely to flee. (FDIC's catalog gives no formula; this is the standard definition.) | $ thousands. |
| `OTHBFHLB` | float64 | OTHER LIABILITIES-FHLB | Advances (secured loans) from the Federal Home Loan Banks; a normal funding source, but heavy or rapidly growing use can signal funding stress (SVB, Signature and First Republic all borrowed heavily in 2022-23). | $ thousands. |
| `VOLIAB` | float64 | VOLATILE LIABILITIES | Funding that can leave quickly: broadly large time deposits, foreign deposits, fed funds purchased and repos, and other borrowed money. (FDIC's catalog gives no formula; this is the standard definition.) | $ thousands. |
| `CHBAL` | float64 | CASH & DUE FROM DEPOSITORY INST | Cash on hand and balances held at other banks: the bank's most immediately available money. | $ thousands. |
| `LNLSDEPR` | float64 | NET LOANS & LEASES/DEPOSITS | Net loans and leases (after the loss allowance) as a share of deposits. High means much of the deposit money is tied up in loans that can't be sold quickly. | Percent. |
| `SCHA` | float64 | SECURITIES-HA | Held-to-maturity securities at amortized cost: bonds the bank plans to keep, carried at purchase price adjusted over time toward face value. Market-value losses on these don't show in equity unless sold. | $ thousands. 0 may mean "not reported". |
| `SCHF` | float64 | TOTAL HELD-TO-MATURITY AT FAIR VALUE SECURITIES ON A CONSOLIDATED BASIS | The same held-to-maturity bonds at current market value. Comparing it with `SCHA` reveals hidden unrealized losses. | $ thousands. 0 may mean "not reported" (SVB: 0 in 2001). |
| `SCAA` | float64 | TOTAL AVAILABLE-FOR-SALE AT AMORTIZED COST SECURITIES ON A CONSOLIDATED BASIS | Available-for-sale securities at purchase-based cost. | $ thousands. 0 may mean "not reported". |
| `SCAF` | float64 | SECURITIES-AF | The same available-for-sale securities at current market value. `SCAA` minus `SCAF` is the unrealized loss. AFS losses hit GAAP equity (via AOCI), but most banks, SVB included, excluded AOCI from regulatory capital, which is why SVB's capital ratios looked healthy. | $ thousands. 0 may mean "not reported". |
| `ingested_at` | datetime (UTC) | (added by Canary) | When Canary pulled this row from the FDIC API; lets you tell which pull a file came from. | Not an FDIC field. Same value for every row in a pull. |
