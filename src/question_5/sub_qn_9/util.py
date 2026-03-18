def write_external_tables(df, spark):
    spark.sql("CREATE DATABASE IF NOT EXISTS db")
    parquet_path = "/tmp/emp_parquet"
    csv_path = "/tmp/emp_csv"
    df.write.mode("overwrite").parquet(parquet_path)
    df.write.mode("overwrite").option("header", True).csv(csv_path)
    spark.sql(f"""
        CREATE TABLE IF NOT EXISTS db.emp_parquet
        USING PARQUET
        LOCATION '{parquet_path}'
    """)
    spark.sql(f"""
        CREATE TABLE IF NOT EXISTS db.emp_csv
        USING CSV
        OPTIONS (header 'true')
        LOCATION '{csv_path}'
    """)