from util import get_spark, get_credit_card_dfs
def main():
    spark = get_spark("credit_cards")
    df1, df2, df3 = get_credit_card_dfs(spark)
    df1.show()
    df2.show()
    df3.show()
if __name__ == "__main__":
    main()