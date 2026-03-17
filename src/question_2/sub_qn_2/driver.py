from src.question_2.sub_qn_1.util import *
from util import num_part

def main():
    spark = get_spark("number_partitions")
    df,_,_= get_credit_card_dfs(spark)
    print(num_part(df))

if __name__ == "__main__":
    main()