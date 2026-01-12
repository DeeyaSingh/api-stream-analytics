from pyspark.sql.functions import col

def apply_dq(df):
    valid = df.filter(
        col("api_name").isNotNull() &
        col("response_time_ms").isNotNull() &
        (col("response_time_ms") > 0)
    )

    invalid = df.subtract(valid)
    return valid, invalid
