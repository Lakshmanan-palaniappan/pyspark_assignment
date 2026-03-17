def write_csv(df, path):
    df.write.mode("overwrite").option("header", True).option("delimiter", ",").csv(path)