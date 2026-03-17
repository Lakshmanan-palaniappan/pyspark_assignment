from src.question_4.sub_qn_1.util import get_spark, read_json
def main():
    spark = get_spark("q1")
    df = read_json(spark)
    df.show(truncate=False)
if __name__ == "__main__":
    main()