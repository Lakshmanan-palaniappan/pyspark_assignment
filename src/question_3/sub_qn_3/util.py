from pyspark.sql.functions import col, count, current_date, to_timestamp, date_sub
def last_7_days(df):
    df = df.withColumn("time_stamp", to_timestamp(col("time_stamp")))
    return df.filter(col("time_stamp") >= date_sub(current_date(), 7)) \
        .groupBy("user_id") \
        .agg(count("*").alias("actions"))