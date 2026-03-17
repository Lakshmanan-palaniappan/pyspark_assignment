import pytest
from src.question_3.sub_qn_1.util import get_spark, get_df
from src.question_3.sub_qn_2.util import rename_cols
@pytest.fixture(scope="session")
def spark():
    s = get_spark("test")
    yield s
    s.stop()
def test_cols(spark):
    df = rename_cols(get_df(spark))
    assert df.columns == ["log_id", "user_id", "user_activity", "time_stamp"]