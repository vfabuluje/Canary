"""Pull each bank's website address (FDIC institutions WEBADDR) into one small Parquet file.

The dashboard shows the bank's website icon next to its name. Only a plain domain is kept
("wellsfargo.com"); anything else is dropped, because the domain goes into the page's markup.
"""

import logging
import re
from pathlib import Path

import pandas as pd

from canary.fdic_client import FDICClient, IncompleteResponseError
from canary.storage import websites_path, write_parquet_atomic

log = logging.getLogger("canary")

_DOMAIN = re.compile(r"^(?=.{4,253}$)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,24}$")


def clean_domain(raw) -> str | None:
    """'https://www.WellsFargo.com/x' -> 'wellsfargo.com'; None for anything that isn't a plain domain."""
    if not isinstance(raw, str):
        return None
    s = raw.strip().lower()
    s = re.sub(r"^[a-z][a-z0-9+.-]*://", "", s)
    s = re.split(r"[/?#]", s, maxsplit=1)[0]
    s = re.sub(r":\d+$", "", s)
    if s.startswith("www."):
        s = s[4:]
    return s if _DOMAIN.match(s) else None


def run_websites(root: Path, client: FDICClient) -> int:
    """Download WEBADDR for every institution (active and inactive) and overwrite the file."""
    records = client.get_all("institutions", {"fields": "CERT,WEBADDR", "sort_by": "CERT", "sort_order": "ASC"})
    if not records:
        raise IncompleteResponseError("API returned 0 rows for institutions")
    df = pd.DataFrame({"cert": [r.get("CERT") for r in records],
                       "website": [clean_domain(r.get("WEBADDR")) for r in records]})
    df = df.dropna().astype({"cert": "int64", "website": "string"}).drop_duplicates("cert").reset_index(drop=True)
    write_parquet_atomic(df, websites_path(root))
    log.info("websites pulled: %s of %s institutions have a usable address", f"{len(df):,}", f"{len(records):,}")
    return len(df)
