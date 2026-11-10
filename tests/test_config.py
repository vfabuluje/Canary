import pytest

from canary.config import ConfigError, load_settings


def test_load_settings_reads_env():
    s = load_settings({"CANARY_BUCKET": "canary-warehouse-abc123"})
    assert s.bucket == "canary-warehouse-abc123"
    assert s.profile == "canary"
    assert s.region == "us-east-1"
    assert s.workgroup == "canary"


def test_profile_from_env():
    s = load_settings({"CANARY_BUCKET": "b", "AWS_PROFILE": "other"})
    assert s.profile == "other"


def test_missing_bucket_raises():
    with pytest.raises(ConfigError):
        load_settings({})


def test_blank_bucket_raises():
    with pytest.raises(ConfigError):
        load_settings({"CANARY_BUCKET": "   "})
