from src.question_5.sub_qn_1.util import get_spark, get_dfs
def main():
    spark = get_spark("q1")
    emp, dept, country = get_dfs(spark)
    emp.show()
    dept.show()
    country.show()
if __name__ == "__main__":
    main()