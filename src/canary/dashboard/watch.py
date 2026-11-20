"""Watchlist size helpers shared by the 2023 and Watchlist pages."""


def published_share(metrics: dict, table: list[dict]) -> float:
    """The watchlist size Canary actually uses: the row of the threshold table that matches the headline run."""
    return next(t["share"] for t in table if t["rows"] == metrics["rows_flagged"])
