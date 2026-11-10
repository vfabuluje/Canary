"""Field lists (single source of truth for which columns are pulled and how they
are typed) and the conversion from API records to a typed DataFrame.

Values are stored exactly as published. The only conversion is "" -> null.
"""

import logging
from typing import NamedTuple

import pandas as pd

logger = logging.getLogger("canary")


class SchemaError(Exception):
    """A value could not be converted to its declared type."""


class Field(NamedTuple):
    dtype: str  # string | int64 | Int64 | float64 | date_ymd | date_mdy
    title: str  # FDIC's own title for the field


# Order matters: ",".join(FINANCIAL_FIELDS) becomes the API `fields=` parameter.
FINANCIAL_FIELDS: dict[str, Field] = {
    "CERT": Field("int64", "FDIC Certificate #"),
    "REPDTE": Field("date_ymd", "Report Date"),
    "NAME": Field("string", "INSTITUTION NAME"),
    "STALP": Field("string", "FIPS STATE ALPHA CODE"),
    "BKCLASS": Field("string", "INSTITUTION CLASS"),
    "NAMEHCR": Field("string", "Bank Holding Company (Regulatory Top Holder)"),
    "ASSET": Field("float64", "Total assets"),
    "LIAB": Field("float64", "TOTAL LIABILITIES"),
    "DEP": Field("float64", "Total deposits"),
    "EQ": Field("float64", "Equity capital"),
    "LNLSGR": Field("float64", "LOANS AND LEASES-TOTAL"),
    "SC": Field("float64", "SECURITIES"),
    "RBC1AAJ": Field("float64", "LEVERAGE RATIO-PCA"),
    "IDT1RWAJR": Field("float64", "TIER 1 RISK-BASED CAPITAL RATIO"),
    "RBCRWAJ": Field("float64", "TOTAL RBC RATIO-PCA"),
    "EQV": Field("float64", "BANK EQUITY CAPITAL/ASSETS"),
    "NCLNLS": Field("float64", "TOTAL N/C-LOANS & LEASES"),
    "NAASSET": Field("float64", "NONACCRUAL-TOTAL ASSETS"),
    "P3ASSET": Field("float64", "30-89 DAYS P/D-TOTAL ASSETS"),
    "P9ASSET": Field("float64", "90+ DAYS P/D-TOTAL ASSETS"),
    "ORE": Field("float64", "OTHER REAL ESTATE OWNED"),
    "LNATRES": Field("float64", "ALLOW FOR LOANS LOSS ADJUSTED"),
    "NTLNLS": Field("float64", "TOTAL LN&LS NET CHARGE-OFFS"),
    "ELNATR": Field("float64", "PROVISIONS FOR CREDIT LOSSES"),
    "LNRE": Field("float64", "RE LOANS"),
    "LNRECONS": Field("float64", "RE CONSTRUCTION & LAND DEVELOP"),
    "LNRENRES": Field("float64", "RE NONFARM NONRESIDENTIAL PROP"),
    "LNCI": Field("float64", "C&I LOANS"),
    "NETINC": Field("float64", "Net income"),
    "ROA": Field("float64", "Return on assets (ROA)"),
    "ROE": Field("float64", "Return on Equity (ROE)"),
    "NIMY": Field("float64", "NET INTEREST MARGIN"),
    "EINTEXP": Field("float64", "TOTAL INTEREST EXPENSE"),
    "EEFFR": Field("float64", "EFFICIENCY RATIO"),
    "DEPUNINS": Field("float64", "ESTIMATED UNINSURED DEPOSITS IN DOMESTIC OFFICES AND IN INSURED BRANCHES IN US TERRITORIES AND POSSESSIONS"),
    "BRO": Field("float64", "BROKERED DEP"),
    "COREDEP": Field("float64", "CORE DEPOSITS"),
    "OTHBFHLB": Field("float64", "OTHER LIABILITIES-FHLB"),
    "VOLIAB": Field("float64", "VOLATILE LIABILITIES"),
    "CHBAL": Field("float64", "CASH & DUE FROM DEPOSITORY INST"),
    "LNLSDEPR": Field("float64", "NET LOANS & LEASES/DEPOSITS"),
    "SCHA": Field("float64", "SECURITIES-HA"),
    "SCHF": Field("float64", "TOTAL HELD-TO-MATURITY AT FAIR VALUE SECURITIES ON A CONSOLIDATED BASIS"),
    "SCAA": Field("float64", "TOTAL AVAILABLE-FOR-SALE AT AMORTIZED COST SECURITIES ON A CONSOLIDATED BASIS"),
    "SCAF": Field("float64", "SECURITIES-AF"),
}

FAILURE_FIELDS: dict[str, Field] = {
    "NAME": Field("string", "Institution Name"),
    "CERT": Field("Int64", "Cert"),
    "FIN": Field("string", "FIN"),
    "CITYST": Field("string", "Location"),
    "FAILDATE": Field("date_mdy", "Effective Date"),
    "FAILYR": Field("Int64", "Year"),
    "SAVR": Field("string", "Insurance Fund"),
    "RESTYPE1": Field("string", "Transaction Type"),
    "CHCLASS1": Field("string", "Charter Class"),
    "RESDATE": Field("date_mdy", "Date of Resolution"),
    "RESTYPE": Field("string", "Resolution"),
    "QBFDEP": Field("float64", "Total Deposits"),
    "QBFASSET": Field("float64", "Total Assets"),
    "COST": Field("float64", "Estimated Loss"),
    "PSTALP": Field("string", "State"),
    "BIDCITY": Field("string", "BIDCITY"),
    "BIDNAME": Field("string", "BIDNAME"),
    "BIDSTATE": Field("string", "BIDSTATE"),
    "CITY": Field("string", "CITY"),
    "FUND": Field("string", "Insurance fund"),
    "PTRDATE": Field("string", "PTRDATE"),
}

_DATE_FORMATS = {"date_ymd": "%Y%m%d", "date_mdy": "%m/%d/%Y"}


def _convert(name: str, values: pd.Series, dtype: str) -> pd.Series:
    try:
        if dtype == "string":
            return values.astype("string")
        if dtype in _DATE_FORMATS:
            parsed = pd.to_datetime(values, format=_DATE_FORMATS[dtype], errors="raise")
            # object column of datetime.date with real None for nulls (.dt.date leaves NaT,
            # and an all-null column would stay a datetime column instead of becoming a date)
            return pd.Series(
                [None if pd.isna(v) else v.date() for v in parsed], index=parsed.index, dtype=object
            )
        nums = pd.to_numeric(values, errors="raise")
        if dtype == "float64":
            return nums.astype("float64")
        if dtype == "Int64":
            return nums.astype("Int64")
        if dtype == "int64":
            if nums.isna().any():
                raise SchemaError(f"{name}: null value in non-nullable int64 field")
            return nums.astype("int64")
    except SchemaError:
        raise
    except (ValueError, TypeError) as exc:
        raise SchemaError(f"{name}: cannot convert to {dtype}: {exc}") from exc
    raise SchemaError(f"{name}: unknown dtype {dtype!r}")


def to_typed_frame(
    records: list[dict], fields: dict[str, Field], ingested_at: pd.Timestamp
) -> pd.DataFrame:
    """Build a typed DataFrame: `fields` columns in order, plus `ingested_at` (UTC)."""
    columns = {}
    for name, field in fields.items():
        raw = [r.get(name) for r in records]
        raw = [None if v == "" else v for v in raw]
        values = pd.Series(raw, dtype=object)
        if records and values.isna().all():
            logger.warning("column %s is null for all %d records", name, len(records))
        columns[name] = _convert(name, values, field.dtype)
    df = pd.DataFrame(columns, index=pd.RangeIndex(len(records)))
    df["ingested_at"] = pd.Series(
        [pd.Timestamp(ingested_at).tz_convert("UTC")] * len(records), dtype="datetime64[ms, UTC]"
    )
    return df
