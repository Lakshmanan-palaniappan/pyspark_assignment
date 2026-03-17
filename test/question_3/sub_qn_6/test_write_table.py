import pytest
from src.question_3.sub_qn_1.util import get_spark, get_df
from src.question_3.sub_qn_2.util import rename_cols
from src.question_3.sub_qn_6.util import write_table
@pytest.fixture(scope="session")
def spark():
    s = get_spark("test_q6")
    yield s
    s.stop()
def test_write_table(spark):
    spark.sql("CREATE DATABASE IF NOT EXISTS user")
    df = rename_cols(get_df(spark))
    write_table(df)
    tables = spark.sql("SHOW TABLES IN user").collect()
    names = [t.tableName for t in tables]
    assert "login_details" in names