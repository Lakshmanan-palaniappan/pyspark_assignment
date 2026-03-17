import pytest
from src.question_4.sub_qn_1.util import get_spark, read_json
from src.question_4.sub_qn_7.util import add_load_date
from src.question_4.sub_qn_8.util import add_ymd
@pytest.fixture(scope="session")
def spark():
    s = get_spark("test_q8")
    yield s
    s.stop()
def test_ymd(spark):
    df = spark.createDataFrame([(1,)], ["id"])
    df = add_load_date(df)
    res = add_ymd(df)
    assert all(col in res.columns for col in ["year", "month", "day"])