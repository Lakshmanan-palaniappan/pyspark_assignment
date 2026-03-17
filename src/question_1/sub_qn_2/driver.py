from src.question_1.sub_qn_1.util import get_spark, get_purchase_df
from src.question_1.sub_qn_2.util import only_iphone13
def main():
    spark = get_spark(session_name="only_iphone13")
    df = get_purchase_df(spark)
    only_iphone13(df).show()
if __name__ == "__main__":
    main()