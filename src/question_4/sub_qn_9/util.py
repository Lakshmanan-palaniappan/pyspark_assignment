def write_table(df):
    df.write.mode("overwrite") \
        .format("json") \
        .partitionBy("year", "month", "day") \
        .option("replaceWhere", "year IS NOT NULL") \
        .saveAsTable("employee.employee_details")