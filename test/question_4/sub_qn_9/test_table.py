import pytest
from src.question_4.sub_qn_1.util import get_spark, read_json
from src.question_4.sub_qn_2.util import flatten
from src.question_4.sub_qn_7.util import add_load_date
from src.question_4.sub_qn_8.util import add_ymd
from src.question_4.sub_qn_9.util import write_table
@pytest.fixture(scope="session")
def spark():
    s = get_spark("test_q9")
    yield s
    s.stop()
def test_write_table(spark):
    spark.sql("CREATE DATABASE IF NOT EXISTS employee")
    df = read_json(spark)
    df = flatten(df)
    df = add_load_date(df)
    df = add_ymd(df)
    write_table(df)
    tables = spark.sql("SHOW TABLES IN employee").collect()
    table_names = [t.tableName for t in tables]
    assert "employee_details" in table_names
def test_table_data(spark):
    df = spark.table("employee.employee_details")
    assert df.count() > 0
def test_partition_columns(spark):
    df = spark.table("employee.employee_details")
    assert all(col in df.columns for col in ["year", "month", "day"])