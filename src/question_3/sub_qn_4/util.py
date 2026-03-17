from pyspark.sql.functions import to_date, col
def add_login_date(df):
    return df.withColumn("login_date", to_date(col("time_stamp")))