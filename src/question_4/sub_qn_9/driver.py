from src.question_4.sub_qn_1.util import get_spark, read_json
from src.question_4.sub_qn_2.util  import flatten
from  src.question_4.sub_qn_7.util import add_load_date
from src.question_4.sub_qn_8.util import add_ymd
from util import write_table
def main():
    spark = get_spark("q9")
    spark.sql("CREATE DATABASE IF NOT EXISTS employee")
    df = read_json(spark)
    df = flatten(df)
    df = add_load_date(df)
    df = add_ymd(df)
    write_table(df)

if __name__ == "__main__":
    main()