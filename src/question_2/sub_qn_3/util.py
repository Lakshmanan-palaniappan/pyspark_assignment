def increase(df):
    return df.repartition(5)