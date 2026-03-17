from src.question_4.sub_qn_1.util import get_spark, read_json
from util import add_load_date
def main():
    spark = get_spark("q7")
    df = read_json(spark)
    add_load_date(df).show()
if __name__ == "__main__":
    main()