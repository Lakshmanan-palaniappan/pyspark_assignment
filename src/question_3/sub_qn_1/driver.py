from src.question_3.sub_qn_1.util import get_spark, get_df
def main():
    spark = get_spark("q1")
    df = get_df(spark)
    df.show()
if __name__ == "__main__":
    main()