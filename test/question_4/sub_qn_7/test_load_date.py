import pytest
from src.question_4.sub_qn_1.util import get_spark
from src.question_4.sub_qn_7.util import add_load_date
@pytest.fixture(scope="session")
def spark():
    s = get_spark("test_q7")
    yield s
    s.stop()
def test_column(spark):
    df = spark.createDataFrame([(1,)], ["id"])
    res = add_load_date(df)

    assert "load_date" in res.columns