import pytest
from src.question_3.sub_qn_1.util import get_spark, get_df
@pytest.fixture(scope="session")
def spark():
    s = get_spark("test_q1")
    yield s
    s.stop()
def test_count(spark):
    df = get_df(spark)
    assert df.count() == 8
def test_schema(spark):
    df = get_df(spark)
    assert df.columns == ["log id", "user$id", "action", "timestamp"]