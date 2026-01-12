from config.spark_config import get_spark
from pyspark.sql.functions import col
from quality.dq_checks import apply_dq

spark = get_spark("SilverClean")

df = (
    spark.readStream
    .format("parquet")
    .load("data/bronze")
    .withWatermark("event_time", "5 minutes")
)

df = df.dropDuplicates(["event_id"])

valid, invalid = apply_dq(df)

(
    invalid.writeStream
    .format("parquet")
    .option("path", "data/dlq")
    .option("checkpointLocation", "data/checkpoints/dlq")
    .start()
)

(
    valid.writeStream
    .format("parquet")
    .option("path", "data/silver")
    .option("checkpointLocation", "data/checkpoints/silver")
    .outputMode("append")
    .start()
)

spark.streams.awaitAnyTermination()
