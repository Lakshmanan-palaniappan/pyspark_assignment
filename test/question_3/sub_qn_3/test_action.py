import pytest
from src.question_3.sub_qn_1.util import get_spark, get_df
from src.question_3.sub_qn_2.util import rename_cols
from src.question_3.sub_qn_3.util import last_7_days
@pytest.fixture(scope="session")
def spark():
    s = get_spark("test")
    yield s
    s.stop()
def test_schema(spark):
    df = rename_cols(get_df(spark))
    res = last_7_days(df)
    assert "user_id" in res.columns