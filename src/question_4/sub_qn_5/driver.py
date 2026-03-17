from src.question_4.sub_qn_1.util import get_spark, read_json
from util import filter_id
def main():
    spark = get_spark("q5")
    df = read_json(spark)
    filter_id(df).show(truncate=False)
if __name__ == "__main__":
    main()