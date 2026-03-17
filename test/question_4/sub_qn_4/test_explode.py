import pytest
from src.question_4.sub_qn_1.util import get_spark, read_json
from src.question_4.sub_qn_4.util import explode_df, explode_outer_df, posexplode_df
@pytest.fixture(scope="session")
def spark():
    s = get_spark("test_q4")
    yield s
    s.stop()
def test_explode_count(spark):
    df = read_json(spark)
    res = explode_df(df)
    assert res.count() == 3
def test_explode_outer_count(spark):
    df = read_json(spark)
    res = explode_outer_df(df)
    assert res.count() == 3
def test_posexplode_columns(spark):
    df = read_json(spark)
    res = posexplode_df(df)
    assert res.columns == ["pos", "col"]