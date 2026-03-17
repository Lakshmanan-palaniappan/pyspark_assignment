from src.question_4.sub_qn_1.util import get_spark, read_json
from util import explode_df, explode_outer_df, posexplode_df
def main():
    spark = get_spark("q4")
    df = read_json(spark)
    print("explode")
    explode_df(df).show(truncate=False)
    print("explode_outer")
    explode_outer_df(df).show(truncate=False)
    print("posexplode")
    posexplode_df(df).show(truncate=False)
if __name__ == "__main__":
    main()