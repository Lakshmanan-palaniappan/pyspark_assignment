import re
def camel_to_snake(name):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
def rename_cols(df):
    return df.toDF(*[camel_to_snake(c) for c in df.columns])