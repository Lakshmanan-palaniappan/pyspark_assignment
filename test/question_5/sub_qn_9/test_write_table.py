import pytest
from src.question_5.sub_qn_1.util import get_spark, get_dfs
from src.question_5.sub_qn_7.util import with_country
from src.question_5.sub_qn_9.util import write_external_tables
@pytest.fixture(scope="session")
def spark():
    s = get_spark("test_q9")
    yield s
    s.stop()
def test_external_tables(spark):
    emp, _, country = get_dfs(spark)
    df = with_country(emp, country)
    write_external_tables(df, spark)
    tables = spark.sql("SHOW TABLES IN db").collect()
    names = [t.tableName for t in tables]
    assert "emp_parquet" in names
    assert "emp_csv" in names