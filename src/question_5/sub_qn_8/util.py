from pyspark.sql.functions import current_date
def lower_and_date(df):
    return df.toDF(*[c.lower() for c in df.columns])\
        .withColumn("load_date",current_date())