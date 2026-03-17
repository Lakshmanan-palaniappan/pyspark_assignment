def rename_cols(df):
    new_cols = ["log_id", "user_id", "user_activity", "time_stamp"]
    return df.toDF(*new_cols)