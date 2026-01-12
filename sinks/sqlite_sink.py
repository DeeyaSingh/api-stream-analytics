import sqlite3
import pandas as pd

def write_to_sqlite(parquet_path):
    df = pd.read_parquet(parquet_path)
    conn = sqlite3.connect("data/api_metrics.db")
    df.to_sql("api_metrics", conn, if_exists="append", index=False)
    conn.close()
