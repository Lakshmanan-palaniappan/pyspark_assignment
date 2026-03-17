from pyspark.sql.functions import col, explode
def flatten(df):
    return df.select(
        col("id"),
        col("properties.name").alias("name"),
        col("properties.storeSize").alias("store_size"),
        explode(col("employees")).alias("emp")
    ).select(
        "id",
        "name",
        "store_size",
        col("emp.empId").alias("emp_id"),
        col("emp.empName").alias("emp_name")
    )