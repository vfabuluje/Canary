-- Raw FDIC quarterly financials: one row per bank per quarter.
-- Columns mirror FINANCIAL_FIELDS (src/canary/schema.py), lower-cased. REPDTE is left out
-- of the column list because the partition column repdte (from the folder name) is the
-- same value and Athena does not allow two columns with the same name.
-- Partition values are listed by 'ALTER TABLE ... SET TBLPROPERTIES' (see athena_ddl.py);
-- the single value below is only a seed. {{bucket}} is filled in by athena_ddl.py.
CREATE EXTERNAL TABLE IF NOT EXISTS canary_raw.fdic_financials (
  cert bigint,
  name string,
  stalp string,
  bkclass string,
  namehcr string,
  asset double,
  liab double,
  dep double,
  eq double,
  lnlsgr double,
  sc double,
  rbc1aaj double,
  idt1rwajr double,
  rbcrwaj double,
  eqv double,
  nclnls double,
  naasset double,
  p3asset double,
  p9asset double,
  ore double,
  lnatres double,
  ntlnls double,
  elnatr double,
  lnre double,
  lnrecons double,
  lnrenres double,
  lnci double,
  netinc double,
  roa double,
  roe double,
  nimy double,
  eintexp double,
  eeffr double,
  depunins double,
  bro double,
  coredep double,
  othbfhlb double,
  voliab double,
  chbal double,
  lnlsdepr double,
  scha double,
  schf double,
  scaa double,
  scaf double,
  ingested_at timestamp
)
PARTITIONED BY (repdte string)
STORED AS PARQUET
LOCATION 's3://{{bucket}}/raw/fdic/financials/'
TBLPROPERTIES (
  'projection.enabled' = 'true',
  'projection.repdte.type' = 'enum',
  'projection.repdte.values' = '20010331',
  'storage.location.template' = 's3://{{bucket}}/raw/fdic/financials/repdte=${repdte}/'
)
