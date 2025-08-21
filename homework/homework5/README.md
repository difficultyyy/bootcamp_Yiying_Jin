# Stage 05: Data Storage

## Folder structure

```python
data/
    processed/
    raw/
```

## Formats

CSV is for human-readable raw drops.  
Parquet is used for efficient, typed, columnar storage in data/processed/

## Environment-driven paths

.env:

```python
DATA_DIR_RAW=data/raw
DATA_DIR_PROCESSED=data/processed
```
