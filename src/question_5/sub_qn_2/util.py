from pyspark.sql.functions import avg
def avg_salary(df):
    return df.groupBy("department").agg(avg("salary").alias("avg_salary"))