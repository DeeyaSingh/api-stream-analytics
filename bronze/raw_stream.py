from config.spark_config import get_spark
from pyspark.sql.functions import col, to_timestamp

spark = get_spark("BronzeIngestion")

schema = """
event_id LONG,
timestamp STRING,
api_name STRING,
response_time_ms INT,
status_code INT,
user_id INT
"""

df = (
    spark.readStream
    .schema(schema)
    .json("data/input")
    .withColumn("event_time", to_timestamp("timestamp"))
)

(
    df.writeStream
    .format("parquet")
    .option("path", "data/bronze")
    .option("checkpointLocation", "data/checkpoints/bronze")
    .outputMode("append")
    .start()
)

spark.streams.awaitAnyTermination()
