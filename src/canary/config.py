"""Project settings: which S3 bucket, AWS profile, region and Athena workgroup to use."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


class ConfigError(Exception):
    """Raised when a required setting is missing."""


@dataclass(frozen=True)
class Settings:
    bucket: str
    region: str = "us-east-1"
    profile: str = "canary"
    workgroup: str = "canary"


def _read_dotenv(path: Path) -> dict[str, str]:
    """Parse a simple KEY=VALUE file. Blank lines and # comments are ignored."""
    values: dict[str, str] = {}
    if not path.is_file():
        return values
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        values[key.strip()] = value.strip().strip("'\"")
    return values


def load_settings(env: Mapping[str, str] | None = None) -> Settings:
    """Build Settings. The repo-root .env is read only when env is None.

    An explicit mapping is used as-is, so tests passing {} never see a real .env.
    """
    if env is None:
        import os

        merged = _read_dotenv(REPO_ROOT / ".env")
        merged.update(os.environ)  # real environment variables win over .env
        env = merged
    bucket = (env.get("CANARY_BUCKET") or "").strip()
    if not bucket:
        raise ConfigError("CANARY_BUCKET is not set. Copy .env.example to .env and fill it in.")
    profile = (env.get("AWS_PROFILE") or "").strip() or "canary"
    return Settings(bucket=bucket, profile=profile)
