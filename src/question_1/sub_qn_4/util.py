from pyspark.sql.functions import *
from pyspark.sql.functions import countDistinct


def new_products(prod_df,pur_df):
    tot=prod_df.select("product_model").distinct().count()

    return pur_df.groupBy("customer").agg(
        countDistinct(
            col("product_model")).alias("count")).filter(
            col("count")==tot
        ).select("customer")