from pyspark.sql.functions import udf, col
from pyspark.sql.types import StringType
def mask(x):
    return "*" * 12 + x[-4:]
mask_udf = udf(mask, StringType())
def mask_df(df):
    return df.withColumn("masked_card_number", mask_udf(col("card_number")))