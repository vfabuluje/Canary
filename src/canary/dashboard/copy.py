"""Fixed dashboard copy. No figures here that the data could contradict; tests check the honest-miss claim."""

CASE_CAPTIONS: dict[int, dict[str, str]] = {
    24735: {
        "before": "Rates were near zero. SVB's bond losses were tiny and Canary ranked it around the middle of the pack. Nothing stood out.",
        "rising": "As rates rose, losses on the bonds SVB planned to hold grew fast. Canary's score went the other way and rated SVB safer.",
        "last": "SVB's last report before it failed: bond losses close to its entire equity, and Canary still rated it safer than most banks. The model learned from 2008-era failures, which looked nothing like this.",
    },
    57053: {
        "before": "Signature grew fast in 2021. Canary put it in the riskier part of the pack, but well short of the watchlist.",
        "rising": "Losses on its bonds for sale grew, and this time the model reacted: the score climbed.",
        "last": "Its last report put it near the top of the list, just short of the watchlist. A bigger watchlist would have flagged it.",
    },
    59017: {
        "before": "Much of First Republic's money came from uninsured deposits: balances above the FDIC limit, which can leave quickly. Canary put it in the riskier part of the pack.",
        "rising": "Its real problem was home loans made at low rates, which lost value as rates rose. FDIC data reports what those loans cost, not what they are worth now, so the model could not see it.",
        "last": "This report came after SVB failed. The uninsured share dropped because depositors had already pulled their money out: the run had started. First Republic failed weeks later.",
    },
}

CASE_LABELS: dict[int, dict[str, str]] = {
    24735: {"chip": "SVB", "name": "Silicon Valley Bank", "failed": "March 10, 2023", "status": "FAILED · NOT FLAGGED"},
    57053: {"chip": "Signature", "name": "Signature Bank", "failed": "March 12, 2023", "status": "FAILED · NEAR MISS"},
    59017: {"chip": "First Republic", "name": "First Republic Bank", "failed": "May 1, 2023", "status": "FAILED · NOT FLAGGED"},
}

WEAK_SPOT_TITLES: dict[int, dict[str, str]] = {
    24735: {
        "title": "Losses on bonds it planned to hold, as a share of the bank's cushion (equity)",
        "note": "The weak spot: the model gave these losses almost no weight.",
    },
    57053: {
        "title": "Losses on bonds it could sell, as a share of the bank's cushion (equity)",
        "note": "Here the model did react.",
    },
    59017: {
        "title": "Deposits above the FDIC insurance limit, as a share of all deposits",
        "note": "High but steady. Its real losses were on home loans, which FDIC data can't value.",
    },
}

HOME_WHAT = (
    "Every three months, US banks publish their numbers. **Canary reads them for every bank in the country and "
    "ranks which ones look most likely to fail within a year**, so trouble can be spotted early. "
    "Like a canary in a coal mine."
)

HONEST_MISS = (
    "In 2023, three large US banks collapsed within two months. **Canary did not flag any of them in time.** "
    "It learned from the 2008 crisis, when banks failed from bad loans. These banks failed differently: their "
    "investments and loans lost value when interest rates rose, and nervous customers pulled their money out fast."
)

# Home headline cards: label and note. Notes may hold {metric} placeholders (format_map over metrics.json);
# the big figure on each card is formatted from metrics.json in the page.
HOME_STATS: dict[str, tuple[str, str]] = {
    "caught": ("FAILURES CAUGHT EARLY", "Banks that failed 2016–2024 that Canary flagged before they failed."),
    "lead": ("TYPICAL HEADS-UP", "How far ahead it flagged the typical bank it caught."),
    "auc": ("RANKING SCORE", "How well it sorts risky from safe (1.00 is perfect). The classic rule of thumb, "
                             "the Texas ratio, scores {baseline[auc]:.2f}."),
    "false_alarm": ("FALSE ALARMS", "Most flagged banks don't fail. Failures are rare, so a watchlist is mostly "
                                    "“keep an eye on it”."),
}

# Home link cards: title and text. {report_count} is the number of exported written reports.
HOME_CARDS: dict[str, tuple[str, str]] = {
    "find": ("🔎 FIND A BANK",
             "Look up any bank's risk rank and history. {report_count} banks have a full written report."),
    "how": ("▶ HOW IT WORKS", "Watch the team of AI helpers and fact-checkers build one, step by step."),
    "watch": ("🎚 WATCHLIST SIZE", "Flag more banks, catch more failures, raise more false alarms. Try it."),
}

# Why Canary. Bodies may hold {metric} placeholders, filled from metrics.json at display time.
WHY_SECTIONS: list[tuple[str, str]] = [
    ("THE NAME",
     "Coal miners used to carry canaries underground. A canary reacts to toxic gas before people do, so if the "
     "canary got sick, the miners knew to get out. **Canary is meant to be that early warning, for banks.**"),
    ("THE STORY BEHIND IT",
     "In 2020 and 2021, Silicon Valley Bank took in billions in deposits from tech startups and put much of it "
     "into long-term government bonds while interest rates were low. In 2022 rates rose fast, and those bonds "
     "lost value. Most of SVB's deposits were above the $250,000 the government insures, so customers had a "
     "reason to run. In March 2023 they pulled about $42 billion in a single day, and regulators closed the bank "
     "on March 10. Signature Bank failed two days later; First Republic in May. **The warning signs were in "
     "SVB's public filings months earlier.**"),
    ("THE GOAL",
     "Could a system built only on public data have raised the alarm in time? Canary reads every US bank's public "
     "numbers each quarter and ranks which look most likely to fail within a year. It learned from failures up to "
     "2015, then was tested on 2016–2024 without peeking. AI helpers write plain-English reports, and every number "
     "they use is checked against the data."),
    ("THE HONEST ANSWER",
     "It caught {banks_caught} of the {eligible_banks} banks that failed in 2016–2024, typically "
     "{lead_time_median:g} quarters ahead. "
     "It did **not** catch SVB, Signature or First Republic. Showing why is part of the point."),
]

# Plain-English meaning of each ratio, shown when a highlighted number is hovered or tapped. Keyed by
# feature column (plus the three concentration tests). No numbers here: the figure comes from the fact.
GLOSSARY: dict[str, str] = {
    "equity_to_assets": "The owners' own money in the bank, compared with everything the bank holds. It is the "
                        "first cushion against losses.",
    "leverage_ratio": "Core capital, the bank's best cushion against losses, compared with its average assets. "
                      "Higher means a thicker cushion.",
    "tier1_risk_based_ratio": "Core capital compared with the bank's assets, where riskier assets count for more. "
                              "Higher means a thicker cushion.",
    "total_risk_based_ratio": "All of the bank's capital compared with its assets, where riskier assets count for "
                              "more. Higher means a thicker cushion.",
    "noncurrent_loans_to_loans": "Loans that are badly behind on payments or no longer earning interest, as a "
                                 "share of all loans.",
    "nonaccrual_ore_to_assets": "Loans no longer earning interest, plus property the bank took back from "
                                "borrowers who stopped paying.",
    "past_due_30_89_to_assets": "Loans that are late on payments, but by less than three months.",
    "allowance_to_loans": "Money the bank has set aside for loans that may not be repaid.",
    "net_charge_offs_to_loans_ann": "Loans the bank gave up on and wrote off over a year, minus anything it "
                                    "later got back.",
    "provision_to_assets_ann": "What the bank added over a year to its reserve for bad loans, compared with "
                               "its size.",
    "construction_loans_to_loans": "Loans that pay for building projects, as a share of all the bank's loans.",
    "cre_loans_to_loans": "Loans tied to commercial property such as offices, stores and apartment buildings, "
                          "as a share of all loans.",
    "texas_ratio": "Troubled loans and repossessed property compared with the bank's capital plus its reserve "
                   "for bad loans. Higher means the trouble is bigger next to the cushion.",
    "return_on_assets": "Yearly profit compared with everything the bank holds.",
    "return_on_equity": "Yearly profit compared with the owners' money in the bank.",
    "net_interest_margin": "What the bank earns on loans and bonds minus what it pays on deposits and borrowing, "
                           "compared with the assets that earn interest. It is the core of how a bank makes money.",
    "efficiency_ratio": "Operating costs as a share of revenue. Lower means the bank runs leaner.",
    "interest_expense_to_assets_ann": "What the bank pays over a year in interest on deposits and borrowing, "
                                      "compared with its size. It goes up when interest rates rise.",
    "loans_to_deposits": "Loans compared with deposits. A high figure means the bank has lent out more than "
                         "its deposits and must fund the rest another way.",
    "uninsured_to_deposits": "Deposits above the government insurance limit. That money is not protected if "
                             "the bank fails, so it can leave quickly.",
    "brokered_to_deposits": "Deposits gathered through middlemen rather than from the bank's own customers. "
                            "They can move elsewhere for a better rate.",
    "core_deposits_to_assets": "Steady, everyday deposits from the bank's own customers, compared with "
                               "everything the bank holds.",
    "fhlb_to_assets": "Loans the bank took from the Federal Home Loan Banks, a government-sponsored lender "
                      "to banks.",
    "volatile_liabilities_to_assets": "Money the bank owes that can leave quickly, such as large deposits and "
                                      "short-term borrowing.",
    "cash_to_assets": "Cash and money held at other banks, ready for depositors who want their money back.",
    "htm_unrealized_loss_to_equity": "How much the bonds the bank planned to keep until they were repaid had "
                                     "lost in value, compared with the owners' money in the bank. These paper "
                                     "losses don't show in reported equity unless the bonds are sold.",
    "afs_unrealized_loss_to_equity": "How much the bonds the bank could sell had lost in value, compared with "
                                     "the owners' money in the bank.",
    "securities_to_assets": "Bonds and similar investments, as a share of everything the bank holds.",
    "log_total_assets": "Everything the bank holds: loans, bonds, cash and the rest. A measure of its size.",
    "asset_growth_4q": "How much the bank grew or shrank over the past year.",
    "deposit_growth_4q": "How much the bank's deposits grew or shrank over the past year.",
    "construction_concentration": "Construction and land loans compared with the bank's capital. Regulators "
                                  "look harder at a bank at or above the line.",
    "cre_concentration": "All commercial real estate loans compared with the bank's capital. Regulators look "
                         "harder at a bank at or above the line whose loans also grew fast.",
    "cre_growth": "How much the bank's commercial real estate loans grew over the prior three years.",
}

# "The short version" on a report page, keyed by the note's outcome. No numbers.
HEADLINES: dict[str, str] = {
    "caught": "Canary flagged {name} before it failed.",
    "missed": "{name} failed, and Canary did not flag it in time.",
    "false_alarm": "Canary flagged {name}, but no failure is on record: a false alarm.",
    "open_watchlist": "{name} is on Canary's watchlist in the latest quarter. The score ranks banks; it does "
                      "not say a bank will fail.",
    "quiet": "Canary did not flag {name}, and no failure is on record.",
}

# Report-card wording for the three 2023 case studies (spec 5.5; ruling R8). Written by Claude in the
# v6 style using only numbers that appear in that bank's note (tests check it); Victor approves it
# before the branch is merged. Each number names the fact it renders ("fact": the fact-sheet label,
# checked against that fact's forms at export) or, for the rule card, a plain "label" (its quarter is the
# as-of quarter unless "quarter" says otherwise; the regulators' lines have none).
_LINE_EXPLAIN = ("Set by US bank regulators in 2006 as a reason for a closer look at a bank, not a "
                 "lending limit.")
_PEER_MEDIAN_EXPLAIN = "The middle figure (the median) for the banks in its peer group."
_NAT_MEDIAN_EXPLAIN = "The middle figure (the median) across all US banks that quarter."

FLAGSHIP_CARDS: dict[int, dict] = {
    24735: {
        "headline": "Canary's score said SVB looked safer than most banks. Its own numbers said otherwise.",
        "cards": {
            "trend": [
                {"text": "Deposits shrank 8.4% in a year.", "numbers": [
                    {"text": "8.4%", "fact": "Trend: deposit growth over the past four quarters, value at the "
                                             "as-of quarter",
                     "explain": "SVB's deposits fell by 8.4% over the past four quarters."}]},
                {"text": "Over the prior 12 quarters, its yearly deposit growth had ranged from 3.8% to 99.7%.",
                 "numbers": [
                    {"text": "3.8%", "fact": "Trend: deposit growth over the past four quarters, lowest value "
                                             "in the comparison window",
                     "explain": "The slowest yearly deposit growth SVB reported in those quarters."},
                    {"text": "99.7%", "fact": "Trend: deposit growth over the past four quarters, highest "
                                              "value in the comparison window",
                     "explain": "The fastest: at its peak, SVB's deposits nearly doubled in a year."}]},
                {"text": "Canary's model took that drop as a reason to lower its score, not raise it.",
                 "numbers": []},
            ],
            "peer": [
                {"text": "In a group of 23 similar big banks, its share of uninsured deposits, 86.4%, was "
                         "unusually high.", "numbers": [
                    {"text": "23", "fact": "Peers: banks in the peer group (including this bank)",
                     "explain": "The FDIC groups SVB with other banks over $10 billion that have no lending "
                                "specialty: 23 banks, SVB included."},
                    {"text": "86.4%", "fact": "Peers: uninsured deposits as a share of deposits, bank value at "
                                              "the as-of quarter",
                     "explain": "86.4% of SVB's deposits were above the government insurance limit. That "
                                "money is not protected if the bank fails, so it can leave quickly."}]},
                {"text": "Typical for those banks: 41.1%.", "numbers": [
                    {"text": "41.1%", "fact": "Peers: uninsured deposits as a share of deposits, peer median",
                     "explain": _PEER_MEDIAN_EXPLAIN}]},
                {"text": "Its paper losses on bonds it planned to hold stood out in the group too.",
                 "numbers": []},
            ],
            "rule": [
                {"text": "The building-loan rule found nothing: SVB did not cross either of the regulators' "
                         "lines.", "numbers": []},
                {"text": "Its commercial real estate loans were only 13.7% of its capital; regulators look "
                         "harder at banks at 300% or more.", "numbers": [
                    {"text": "13.7%", "label": "Total commercial real estate loans ÷ capital",
                     "explain": "Loans tied to offices, stores, apartments and building projects, compared "
                                "with SVB's capital (Tier 1 capital plus its reserve for bad loans)."},
                    {"text": "300%", "label": "Regulators' line for commercial real estate loans", "quarter": None,
                     "explain": _LINE_EXPLAIN}]},
                {"text": "That kind of lending simply wasn't SVB's problem.", "numbers": []},
            ],
            "summary": [
                {"text": "Its loans looked clean, but its funding and bonds stood out.", "numbers": []},
                {"text": "Uninsured deposits were 86.4% of its deposits, against 25.5% at a typical bank, and "
                         "paper losses on bonds it planned to hold equaled 98.1% of its equity.", "numbers": [
                    {"text": "86.4%", "fact": "Bank: uninsured deposits as a share of deposits",
                     "explain": "86.4% of SVB's deposits were above the government insurance limit. That "
                                "money is not protected if the bank fails, so it can leave quickly."},
                    {"text": "25.5%", "fact": "National median: uninsured deposits as a share of deposits",
                     "explain": _NAT_MEDIAN_EXPLAIN},
                    {"text": "98.1%", "fact": "Bank: losses on bonds held to maturity, as a share of equity",
                     "explain": "SVB's bonds had lost value since it bought them. On paper, the losses equaled "
                                "98.1% of its equity, the owners' cushion against losses. Because SVB planned "
                                "to keep the bonds until they were repaid, the losses did not show in its "
                                "reported equity."}]},
                {"text": "Canary's calm score and these numbers point in different directions, and the report "
                         "says so instead of hiding it.", "numbers": []},
            ],
        },
    },
    57053: {
        "headline": "Canary rated Signature riskier than most banks, but not risky enough for its watchlist.",
        "cards": {
            "trend": [
                {"text": "Volatile funding, money that can leave quickly, jumped to 14.7% of its assets.",
                 "numbers": [
                    {"text": "14.7%", "fact": "Trend: volatile funding as a share of assets, value at the "
                                              "as-of quarter",
                     "explain": "Money Signature owed that could leave quickly, such as large deposits and "
                                "short-term borrowing, was 14.7% of everything it held."}]},
                {"text": "In the prior 12 quarters it had ranged from 2.6% to 9.9%.", "numbers": [
                    {"text": "2.6%", "fact": "Trend: volatile funding as a share of assets, lowest value in "
                                             "the comparison window",
                     "explain": "The lowest share Signature reported in those quarters."},
                    {"text": "9.9%", "fact": "Trend: volatile funding as a share of assets, highest value in "
                                             "the comparison window",
                     "explain": "The highest share in those quarters, before this one."}]},
                {"text": "Deposits shrank 16.5% in a year.", "numbers": [
                    {"text": "16.5%", "fact": "Trend: deposit growth over the past four quarters, value at the "
                                              "as-of quarter",
                     "explain": "Signature's deposits fell by 16.5% over the past four quarters."}]},
                {"text": "Canary's model took both changes as reasons to lower its score, not raise it.",
                 "numbers": []},
            ],
            "peer": [
                {"text": "In a group of 113 similar big banks, its share of uninsured deposits, 89.7%, was "
                         "unusually high.", "numbers": [
                    {"text": "113", "fact": "Peers: banks in the peer group (including this bank)",
                     "explain": "The FDIC groups Signature with other commercial lenders over $10 billion: "
                                "113 banks, Signature included."},
                    {"text": "89.7%", "fact": "Peers: uninsured deposits as a share of deposits, bank value at "
                                              "the as-of quarter",
                     "explain": "89.7% of Signature's deposits were above the government insurance limit. "
                                "That money is not protected if the bank fails, so it can leave quickly."}]},
                {"text": "Typical for those banks: 44.3%.", "numbers": [
                    {"text": "44.3%", "fact": "Peers: uninsured deposits as a share of deposits, peer median",
                     "explain": _PEER_MEDIAN_EXPLAIN}]},
                {"text": "Its deposit growth, -16.5%, was among the lowest in the group, where the typical "
                         "figure was -0.6%.", "numbers": [
                    {"text": "-16.5%", "fact": "Peers: deposit growth over the past four quarters, bank value "
                                               "at the as-of quarter",
                     "explain": "Signature's deposits fell by 16.5% over the past four quarters."},
                    {"text": "-0.6%", "fact": "Peers: deposit growth over the past four quarters, peer median",
                     "explain": _PEER_MEDIAN_EXPLAIN}]},
            ],
            "rule": [
                {"text": "Its commercial real estate loans were 314.5% of its capital, over the 300% line "
                         "regulators use.", "numbers": [
                    {"text": "314.5%", "label": "Total commercial real estate loans ÷ capital",
                     "explain": "Loans tied to offices, stores, apartments and building projects, compared "
                                "with Signature's capital (Tier 1 capital plus its reserve for bad loans)."},
                    {"text": "300%", "label": "Regulators' line for commercial real estate loans", "quarter": None,
                     "explain": _LINE_EXPLAIN}]},
                {"text": "But the screen also needs those loans to have grown 50% or more over 36 months, and "
                         "they grew 24.6%, so Signature did not cross the line.", "numbers": [
                    {"text": "50%", "label": "Regulators' growth line for commercial real estate loans",
                     "quarter": None, "explain": _LINE_EXPLAIN},
                    {"text": "24.6%", "label": "Growth in commercial real estate loans over the prior 36 months",
                     "explain": "How much Signature's commercial real estate loans grew over the prior "
                                "36 months."}]},
                {"text": "Its construction loans were 15.6% of its capital, far under the 100% line.",
                 "numbers": [
                    {"text": "15.6%", "label": "Construction and land loans ÷ capital",
                     "explain": "Loans that pay for building projects and land, compared with Signature's "
                                "capital."},
                    {"text": "100%", "label": "Regulators' line for construction loans", "quarter": None,
                     "explain": _LINE_EXPLAIN}]},
            ],
            "summary": [
                {"text": "Its loan problems were close to typical, but its funding stood out: 89.7% of its "
                         "deposits were uninsured, against 25.5% at a typical bank.", "numbers": [
                    {"text": "89.7%", "fact": "Bank: uninsured deposits as a share of deposits",
                     "explain": "89.7% of Signature's deposits were above the government insurance limit. "
                                "That money is not protected if the bank fails, so it can leave quickly."},
                    {"text": "25.5%", "fact": "National median: uninsured deposits as a share of deposits",
                     "explain": _NAT_MEDIAN_EXPLAIN}]},
                {"text": "The biggest push toward a higher score came from losses on bonds it could sell, "
                         "equal to 30.6% of its equity.", "numbers": [
                    {"text": "30.6%", "fact": "Bank: losses on bonds available for sale, as a share of equity",
                     "explain": "Bonds Signature could sell had lost value since it bought them. The losses "
                                "equaled 30.6% of its equity, the owners' cushion against losses."}]},
                {"text": "Several of its funding changes pushed the score down instead, so the numbers and the "
                         "model point different ways.", "numbers": []},
            ],
        },
    },
    59017: {
        "headline": "First Republic's deposits were draining away. Canary's score rose, but not enough for "
                    "its watchlist.",
        "cards": {
            "trend": [
                {"text": "Core deposits, the steady everyday money, fell to 25.2% of its assets.", "numbers": [
                    {"text": "25.2%", "fact": "Trend: core deposits as a share of assets, value at the as-of "
                                              "quarter",
                     "explain": "Steady, everyday deposits from First Republic's own customers were 25.2% of "
                                "everything it held."}]},
                {"text": "In the prior 12 quarters that share had ranged from 68.5% to 84.0%.", "numbers": [
                    {"text": "68.5%", "fact": "Trend: core deposits as a share of assets, lowest value in the "
                                              "comparison window",
                     "explain": "The lowest share First Republic reported in those quarters."},
                    {"text": "84.0%", "fact": "Trend: core deposits as a share of assets, highest value in the "
                                              "comparison window",
                     "explain": "The highest share in those quarters."}]},
                {"text": "Volatile funding, money that can leave quickly, jumped to 53.0% of its assets, from "
                         "a prior range of 2.4% to 11.4%.", "numbers": [
                    {"text": "53.0%", "fact": "Trend: volatile funding as a share of assets, value at the "
                                              "as-of quarter",
                     "explain": "Money First Republic owed that could leave quickly, such as large deposits "
                                "and short-term borrowing, was 53.0% of everything it held."},
                    {"text": "2.4%", "fact": "Trend: volatile funding as a share of assets, lowest value in "
                                             "the comparison window",
                     "explain": "The lowest share First Republic reported in the prior 12 quarters."},
                    {"text": "11.4%", "fact": "Trend: volatile funding as a share of assets, highest value in "
                                              "the comparison window",
                     "explain": "The highest share in those quarters, before this one."}]},
                {"text": "Canary's model took both changes as reasons to raise its score.", "numbers": []},
                {"text": "A year earlier the bank sat at the 28.0th percentile; by this report it was at the "
                         "83.0th.", "numbers": [
                    {"text": "28.0th", "fact": "Percentile a year earlier (100 = highest risk)",
                     "explain": "Where Canary's score put First Republic a year earlier, on a scale of 0 to "
                                "100 where higher means riskier."},
                    {"text": "83.0th", "fact": "Percentile (100 = highest risk)",
                     "explain": "Where Canary's score put First Republic in this report: riskier than most "
                                "banks, but short of the watchlist, which covers the top 2%."}]},
            ],
            "peer": [
                {"text": "In a group of 24 similar big banks, its volatile funding, 53.0% of its assets, was "
                         "unusually high.", "numbers": [
                    {"text": "24", "fact": "Peers: banks in the peer group (including this bank)",
                     "explain": "The FDIC groups First Republic with other banks over $10 billion that have "
                                "no lending specialty: 24 banks, First Republic included."},
                    {"text": "53.0%", "fact": "Peers: volatile funding as a share of assets, bank value at the "
                                              "as-of quarter",
                     "explain": "Money First Republic owed that could leave quickly was 53.0% of everything "
                                "it held."}]},
                {"text": "Typical for those banks: 5.7%.", "numbers": [
                    {"text": "5.7%", "fact": "Peers: volatile funding as a share of assets, peer median",
                     "explain": _PEER_MEDIAN_EXPLAIN}]},
                {"text": "Its loans were 165.1% of its deposits, against 63.2% for the typical bank in the "
                         "group.", "numbers": [
                    {"text": "165.1%", "fact": "Peers: loans as a share of deposits, bank value at the as-of "
                                               "quarter",
                     "explain": "First Republic had lent out more than it held in deposits, so the rest of "
                                "its lending had to be funded another way."},
                    {"text": "63.2%", "fact": "Peers: loans as a share of deposits, peer median",
                     "explain": _PEER_MEDIAN_EXPLAIN}]},
            ],
            "rule": [
                {"text": "The building-loan rule found nothing: First Republic did not cross either of the "
                         "regulators' lines.", "numbers": []},
                {"text": "Its commercial real estate loans were 200.7% of its capital, under the 300% line.",
                 "numbers": [
                    {"text": "200.7%", "label": "Total commercial real estate loans ÷ capital",
                     "explain": "Loans tied to offices, stores, apartments and building projects, compared "
                                "with First Republic's capital (Tier 1 capital plus its reserve for bad "
                                "loans)."},
                    {"text": "300%", "label": "Regulators' line for commercial real estate loans", "quarter": None,
                     "explain": _LINE_EXPLAIN}]},
                {"text": "This screen looks for heavy lending on commercial property, a more common way banks "
                         "have failed; it didn't find that here.", "numbers": []},
            ],
            "summary": [
                {"text": "Its funding stood out sharply: volatile funding was 53.0% of its assets, against "
                         "6.5% at a typical bank.", "numbers": [
                    {"text": "53.0%", "fact": "Bank: volatile funding as a share of assets",
                     "explain": "Money First Republic owed that could leave quickly was 53.0% of everything "
                                "it held."},
                    {"text": "6.5%", "fact": "National median: volatile funding as a share of assets",
                     "explain": _NAT_MEDIAN_EXPLAIN}]},
                {"text": "Its clean loans and its capital ratio looked healthy to the model and pulled its "
                         "score down.", "numbers": []},
                {"text": "The two point in different directions, and the report says so instead of blending "
                         "them.", "numbers": []},
            ],
        },
    },
}


# ------------------------------------------------------------------------- 2023 and Watchlist pages
CASES_TITLE = "THE 2023 COLLAPSES"
CASES_LEDE = ("Each bank, quarter by quarter, in the two years before it failed. Top: how risky Canary thought it was. "
              "Bottom: the bank's real weak spot. Drag the slider or tap a point.")
CASES_SCORE_TITLE = "Canary's risk rating (higher = riskier)"
CASES_SCORE_NOTE = "Dashed line: the watchlist. Above it, Canary would have flagged the bank."
CASES_SLIDER_LABEL = "Quarter"
CASES_SIDE = {
    "report": "{quarter} REPORT",
    "of": "riskiest of {n:,} banks (#1 = riskiest)",
    "rating": "Risk rating",
    "on_list": "On the watchlist?",
    "yes": "YES",
    "no": "No",
    "bars": "WHAT PUSHED THE RATING UP MOST",
}
WEAK_SHORT_LABELS: dict[int, str] = {24735: "Bond losses vs. equity", 57053: "Bond losses vs. equity",
                                     59017: "Uninsured deposits"}

WATCH_TITLE = "HOW BIG SHOULD THE WATCHLIST BE?"
WATCH_LEDE = ("Each quarter Canary flags its riskiest slice of banks. Flag more, and you catch more failures, but you "
              "also flag more banks that turn out fine. Pick a size. The numbers are recalculated from the real "
              "2016-2024 test.")
WATCH_PUBLISHED = "★ CANARY USES THIS"
WATCH_CARDS = {
    "caught": ("FAILURES CAUGHT EARLY", "Out of {eligible} banks that failed 2016-2024."),
    "false_alarm": ("FALSE ALARMS", "Share of flags where the bank did not fail within a year."),
    "flags": ("FLAGS RAISED", "Bank-quarters flagged, 2016-2024."),
}
WATCH_CHART_TITLE = "Failures caught, by watchlist size"
WATCH_CHART_NOTE = "Highlighted: the size you picked."
WATCH_SAY = "Flagging the **top {share}%** each quarter catches **{caught} of {eligible}** failures early. {cases}"
WATCH_CASES_CAUGHT = "At this size **{caught} would have been caught**.{missed}"
WATCH_CASES_MISSED = " {missed} still would not."
WATCH_CASES_NONE = "None of the three 2023 collapses is caught at this size."

FIND_TITLE = "FIND A BANK"
FIND_LEDE = "Search any US bank that has filed a report with the FDIC, past or present."
FIND_LABEL = "Bank name"
FIND_PLACEHOLDER = "Find a bank, e.g. SVB"
FIND_HINT = "Try “SVB”, “Chase” or “IndyMac”."
FIND_DID_YOU_MEAN = "Did you mean one of these?"
FIND_NOT_CLOSE = ("No bank with that name in the FDIC data. Canary covers FDIC-insured banks, so credit unions "
                  "aren't included. The closest names:")
FIND_NONE = "No bank found. Check the spelling, or try part of the name."
FIND_BAD_CERT = "No bank found for that certificate number."
FIND_BACK = "◀ SEARCH AGAIN"
BANK_NO_REPORT = "No written report for this bank"
BANK_NO_REPORT_NOTE = "Canary has not written a report for this bank. Here is its latest rating and how it has moved."
BANK_LATEST = "Latest report: **{quarter}**. Ranked **#{rank:,}** of {n:,} banks (1 = riskiest); risk rating **{rating:.1f} out of {scale}**."
BANK_AFTER_TEST = "This quarter is after the test period, so it was not part of Canary's tested results."
BANK_FLAGGED = "On the watchlist that quarter."
BANK_HISTORY_TITLE = "Risk rating by quarter (higher = riskier)"
BANK_CONCENTRATION_TITLE = "Commercial real estate check"
BANK_CONCENTRATION_REASON = "The check can't be applied for the latest quarter: {reason}."
BANK_CONCENTRATION_NONE = "No commercial real estate check is available for this bank."
BANK_UNSCORED = ("Canary only scores banks from 2016 on; this bank stopped reporting in {year}, before that. "
                 "Earlier years were used to train the model, so scoring them would not be a fair test.")
BANK_FULL_REPORT = "Read the full report"
BANK_FAILED = "Failed {date}"

# Ask Canary (the box on each written-report page). Limits are filled in from canary.dashboard.ask.
ASK_TITLE = "Ask Canary about this bank"
ASK_LABEL = "Your question"
ASK_PLACEHOLDER = "e.g. How much of its deposits were uninsured?"
ASK_BUTTON = "ASK"
ASK_THINKING = "Reading this bank's facts and checking the answer..."
ASK_NOTE = "Answers are written by AI from this bank's public data, fact-checked, and not financial advice."
ASK_RESTING = "Ask Canary is resting for today."
ASK_CANT_CHECK = "I couldn't answer that with checked facts."
ASK_EMPTY = "Type a question first."
ASK_TOO_LONG = "That question is {count:,} characters long. Please keep it to {limit:,} characters or fewer."
ASK_LEFT = "Questions left this visit: {left} of {limit}."
ASK_SESSION_DONE = "You've asked all {limit} questions for this visit. Thanks for trying Ask Canary!"

HOW_TITLE = "HOW IT WORKS"
HOW_LEDE = ("Watch Canary's AI team build a real report, one step at a time. Then see how the whole system fits "
            "together, from public data to checked numbers.")
HOW_PICK = "Watch the report being built for"
HOW_STRIP_TITLE = "Canary, end to end"
# (title, one plain line, "AI" or "CODE")
HOW_STEPS = [
    ("Public FDIC data", "Every insured bank's quarterly numbers, from the FDIC's free public data.", "CODE"),
    ("The model ranks every bank", "Each quarter a machine-learning model scores every bank, and code ranks them "
                                   "from riskiest to safest.", "CODE"),
    ("An AI team writes reports", "For the showcase banks, AI helpers write a plain-English report on what stands "
                                  "out.", "AI"),
    ("Every number is checked", "Code checks each number the AI wrote against the bank's own data before the "
                                "report is saved.", "CODE"),
]
HOW_MARKS = {"AI": "an AI helper writes this part", "CODE": "plain code, no AI"}
