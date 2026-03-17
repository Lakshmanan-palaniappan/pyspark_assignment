from src.question_2.sub_qn_1.util import get_spark, get_credit_card_dfs
from util import mask_df
def main():
    spark = get_spark("q5")
    df, _, _ = get_credit_card_dfs(spark)
    mask_df(df).show(truncate=False)
if __name__ == "__main__":
    main()