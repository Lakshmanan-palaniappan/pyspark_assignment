from src.question_4.sub_qn_1.util import get_spark, read_json
from src.question_4.sub_qn_7.util import add_load_date
from util import add_ymd
def main():
    spark = get_spark("q8")
    df = read_json(spark)
    df = add_load_date(df)
    add_ymd(df).show()
if __name__ == "__main__":
    main()