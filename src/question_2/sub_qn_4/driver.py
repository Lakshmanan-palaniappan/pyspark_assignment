from src.question_2.sub_qn_1.util import get_spark, get_credit_card_dfs
from util import decrease
def main():
    spark = get_spark("q4")
    df, _, _ = get_credit_card_dfs(spark)
    orig = df.rdd.getNumPartitions()
    df2 = df.repartition(5)
    print(decrease(df2, orig).rdd.getNumPartitions())
if __name__ == "__main__":
    main()