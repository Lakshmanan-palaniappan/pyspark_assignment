from src.question_2.sub_qn_1.util import get_spark, get_credit_card_dfs
from util import increase
def main():
    spark = get_spark("increase")
    df, _, _ = get_credit_card_dfs(spark)
    print(increase(df).rdd.getNumPartitions())
if __name__ == "__main__":
    main()