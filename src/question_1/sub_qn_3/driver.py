from src.question_1.sub_qn_1.util import get_spark,get_purchase_df
from util import upgrade_to_iphone14

def main():
    spark = get_spark("upgrade_to_iphone14")
    df = get_purchase_df(spark)
    upgrade_to_iphone14(df).show(truncate=False)
if __name__ == "__main__":
    main()