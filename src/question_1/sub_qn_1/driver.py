from util import get_spark, get_purchase_df, get_product_df
def main():
    spark = get_spark("creation")
    purchase_df = get_purchase_df(spark)
    product_df = get_product_df(spark)
    purchase_df.show()
    product_df.show()
if __name__ == "__main__":
    main()