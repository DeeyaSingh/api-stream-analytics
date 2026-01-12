from pyspark.sql.functions import col

def add_sla_flags(df):
    return df.withColumn(
        "sla_violation",
        col("p95_latency") > 500
    )
