from pyspark.sql.functions import *
def upgrade_to_iphone14(df):
    agg_df = df.groupBy("customer").agg(collect_set("product_model").alias("products"))
    return agg_df.withColumn(
        "upgraded",
        when(array_contains(col("products"), "iphone13") & array_contains(col("products"), "iphone14"),
             "Yes").otherwise("No")
    ).filter(col("upgraded") == "Yes").select("customer", "upgraded", "products")
