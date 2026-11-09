# fdic_financials

Quarterly financial snapshot of every FDIC-insured bank, as published by the FDIC.

| | |
|---|---|
| Grain | One row per bank (`CERT`) per quarter (`REPDTE`) |
| Primary key | (`CERT`, `REPDTE`) |
| Source | `GET https://api.fdic.gov/banks/financials` (FDIC BankFind) |
| File | `data/raw/financials/repdte=YYYYMMDD/part.parquet` (one file per quarter) |
| Rows | _filled in after the first full pull_ |

Design and reasoning: [[specs/2026-11-09-phase1-fdic-ingestion-design]]. Column names are FDIC's own, kept as-is so each can be looked up in FDIC docs. Values are stored exactly as published; the only conversion is blank to null.

## Read this before using the data

- **Dollar amounts are in thousands of dollars.** SVB's `ASSET` of 209,026,000 means $209 billion.
- **Ratios are percent.** A `ROA` of 7.96 means 7.96%, not 0.0796.
- **Income fields are year-to-date.** Q4 covers the whole year, Q1 covers one quarter. This applies to `NETINC`, `EINTEXP`, `ELNATR`, `NTLNLS` and ratios built on them (`ROA`, `ROE`, `NIMY`, `EEFFR`). Phase 3 must convert them to per-quarter values.
- **0 can mean "not reported".** Some fields did not exist in early years (SVB's `SCHF` is 0 in 2001). Phase 1 keeps the 0; Phase 3 decides how to treat it.
- **Current, amended values only.** The API serves the latest corrected numbers for every quarter, not what the bank originally filed. A replay of SVB therefore uses numbers as corrected later, not exactly what an analyst saw in early 2023.
- **Blank is stored as null**, not as an empty string.

## Columns

| Column | Type | FDIC title | Meaning (plain English) | Units / caveats |
|---|---|---|---|---|
| `CERT` | int64 | FDIC Certificate # | The bank's unique FDIC ID number; the key for joining to the failures table. | Never null here. |
| `REPDTE` | date | Report Date | The quarter-end date this snapshot describes. | Stored as a real date (e.g. 2022-12-31). |
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
| `P3ASSET` | float64 | 30-89 DAYS P/D-TOTAL ASSETS | Assets whose payments are 30 to 89 days late: an early sign of borrower trouble. | $ thousands. |
| `P9ASSET` | float64 | 90+ DAYS P/D-TOTAL ASSETS | Assets whose payments are 90 or more days late: a more serious sign of borrower trouble. | $ thousands. |
| `ORE` | float64 | OTHER REAL ESTATE OWNED | Property the bank has taken over after borrowers defaulted (foreclosed real estate). | $ thousands. |
| `LNATRES` | float64 | ALLOW FOR LOANS LOSS ADJUSTED | The reserve the bank has set aside to cover expected loan losses. | $ thousands. |
| `NTLNLS` | float64 | TOTAL LN&LS NET CHARGE-OFFS | Loans written off as uncollectible, minus later recoveries. | $ thousands. Year-to-date. |
| `ELNATR` | float64 | PROVISIONS FOR CREDIT LOSSES | Money the bank charged against earnings to add to its loan-loss reserve. | $ thousands. Year-to-date. |
| `LNRE` | float64 | RE LOANS | Loans secured by real estate. | $ thousands. |
| `LNRECONS` | float64 | RE CONSTRUCTION & LAND DEVELOP | Loans for building projects and land development, historically a risky category. | $ thousands. |
| `LNRENRES` | float64 | RE NONFARM NONRESIDENTIAL PROP | Commercial real estate loans (office buildings, shops, and similar, not homes or farms). | $ thousands. |
| `LNCI` | float64 | C&I LOANS | Commercial and industrial loans: loans to businesses for their operations. | $ thousands. |
| `NETINC` | float64 | Net income | Profit after all expenses and taxes. | $ thousands. Year-to-date. |
| `ROA` | float64 | Return on assets (ROA) | Profit as a share of assets: how efficiently the bank earns money. | Percent. Year-to-date basis. |
| `ROE` | float64 | Return on Equity (ROE) | Profit as a share of owners' equity. | Percent. Year-to-date basis. |
| `NIMY` | float64 | NET INTEREST MARGIN | Interest earned on loans and securities minus interest paid on deposits and borrowings, as a share of earning assets. A squeezed margin hurts profits. | Percent. Year-to-date basis. |
| `EINTEXP` | float64 | TOTAL INTEREST EXPENSE | Total interest the bank paid on deposits and borrowings. | $ thousands. Year-to-date. |
| `EEFFR` | float64 | EFFICIENCY RATIO | Operating costs per dollar of revenue; lower means the bank spends less to earn each dollar. | Percent. Year-to-date basis. |
| `DEPUNINS` | float64 | ESTIMATED UNINSURED DEPOSITS IN DOMESTIC OFFICES AND IN INSURED BRANCHES IN US TERRITORIES AND POSSESSIONS | Estimated deposits above the $250K insurance limit. These customers have the most reason to flee in a panic, which is what sank SVB. | $ thousands. An estimate; likely null or 0 in early years. |
| `BRO` | float64 | BROKERED DEP | Deposits the bank obtained through brokers rather than directly from customers; often more rate-sensitive and quicker to leave. | $ thousands. |
| `COREDEP` | float64 | CORE DEPOSITS | Stable, everyday deposits, generally less likely to flee. | $ thousands. |
| `OTHBFHLB` | float64 | OTHER LIABILITIES-FHLB | Borrowings from the Federal Home Loan Bank, a source of emergency-style funding that signals reliance on borrowed money. | $ thousands. |
| `VOLIAB` | float64 | VOLATILE LIABILITIES | Funding that can leave quickly, such as large uninsured deposits and short-term borrowings. | $ thousands. |
| `CHBAL` | float64 | CASH & DUE FROM DEPOSITORY INST | Cash on hand and balances held at other banks: the bank's most immediately available money. | $ thousands. |
| `LNLSDEPR` | float64 | NET LOANS & LEASES/DEPOSITS | Loans as a share of deposits. High means much of the deposit money is tied up in loans that can't be sold quickly. | Percent. |
| `SCHA` | float64 | SECURITIES-HA | Held-to-maturity securities at amortized cost: bonds the bank plans to keep, recorded at purchase value. Losses on these don't show in equity until sold. | $ thousands. 0 may mean "not reported". |
| `SCHF` | float64 | TOTAL HELD-TO-MATURITY AT FAIR VALUE SECURITIES ON A CONSOLIDATED BASIS | The same held-to-maturity bonds at current market value. Comparing it with `SCHA` reveals hidden unrealized losses. | $ thousands. 0 may mean "not reported" (SVB: 0 in 2001). |
| `SCAA` | float64 | TOTAL AVAILABLE-FOR-SALE AT AMORTIZED COST SECURITIES ON A CONSOLIDATED BASIS | Available-for-sale securities at purchase-based cost. | $ thousands. 0 may mean "not reported". |
| `SCAF` | float64 | SECURITIES-AF | The same available-for-sale securities at current market value. `SCAA` minus `SCAF` is the unrealized loss. | $ thousands. 0 may mean "not reported". |
| `ingested_at` | datetime (UTC) | (added by Canary) | When Canary pulled this row from the FDIC API; lets you tell which pull a file came from. | Not an FDIC field. Same value for every row in a pull. |
