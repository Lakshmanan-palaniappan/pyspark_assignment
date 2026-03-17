def write_table(df):
    df.write.mode("overwrite").saveAsTable("user.login_details")