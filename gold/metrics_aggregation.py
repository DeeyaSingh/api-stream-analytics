from config.spark_config import get_spark
from pyspark.sql.functions import (
    window, avg, count, expr, percentile_approx
)

spark = get_spark("GoldMetrics")

df = spark.readStream.format("parquet").load("data/silver")

metrics = (
    df.groupBy(
        window("event_time", "1 minute", "30 seconds"),
        "api_name"
    )
    .agg(
        count("*").alias("request_count"),
        avg("response_time_ms").alias("avg_latency"),
        percentile_approx("response_time_ms", 0.95).alias("p95_latency"),
        expr("sum(case when status_code >= 400 then 1 else 0 end) / count(*)")
        .alias("error_rate")
    )
)

(
    metrics.writeStream
    .format("parquet")
    .partitionBy("api_name")
    .option("path", "data/gold")
    .option("checkpointLocation", "data/checkpoints/gold")
    .outputMode("append")
    .start()
)

spark.streams.awaitAnyTermination()
