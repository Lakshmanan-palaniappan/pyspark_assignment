from src.question_4.sub_qn_1.util import get_spark, read_json
from util import rename_cols
def main():
    spark = get_spark("q6")
    df = read_json(spark)
    rename_cols(df).show()
if __name__ == "__main__":
    main()