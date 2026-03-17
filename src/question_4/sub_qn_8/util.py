from pyspark.sql.functions import year, month, dayofmonth, col
def add_ymd(df):
    return df.withColumn("year", year(col("load_date"))) \
             .withColumn("month", month(col("load_date"))) \
             .withColumn("day", dayofmonth(col("load_date")))