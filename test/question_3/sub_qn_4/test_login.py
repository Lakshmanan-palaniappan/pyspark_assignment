import pytest
from src.question_3.sub_qn_1.util import get_spark, get_df
from src.question_3.sub_qn_2.util import rename_cols
from src.question_3.sub_qn_4.util import add_login_date
@pytest.fixture(scope="session")
def spark():
    s = get_spark("test")
    yield s
    s.stop()
def test_col_exists(spark):
    df = rename_cols(get_df(spark))
    res = add_login_date(df)
    assert "login_date" in res.columns