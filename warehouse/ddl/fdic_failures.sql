-- Raw FDIC failed-bank list: one row per failed institution since 2000.
-- Columns mirror FAILURE_FIELDS (src/canary/schema.py), lower-cased.
CREATE EXTERNAL TABLE IF NOT EXISTS canary_raw.fdic_failures (
  name string,
  cert bigint,
  fin string,
  cityst string,
  faildate date,
  failyr bigint,
  savr string,
  restype1 string,
  chclass1 string,
  resdate date,
  restype string,
  qbfdep double,
  qbfasset double,
  cost double,
  pstalp string,
  bidcity string,
  bidname string,
  bidstate string,
  city string,
  fund string,
  ptrdate string,
  ingested_at timestamp
)
STORED AS PARQUET
LOCATION 's3://{{bucket}}/raw/fdic/failures/'
