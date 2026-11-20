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
    "bond investments lost value when interest rates rose, and nervous customers pulled their money out fast."
)

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
     "It caught 21 of the 29 banks that failed in 2016–2024, usually about a year ahead. It did **not** catch SVB, "
     "Signature or First Republic. Showing why is part of the point."),
]
