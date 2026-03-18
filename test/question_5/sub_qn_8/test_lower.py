import pytest
from src.question_5.sub_qn_1.util import get_spark, get_dfs
from src.question_5.sub_qn_7.util import with_country
from src.question_5.sub_qn_8.util import lower_and_date
@pytest.fixture(scope="session")
def spark():
    s = get_spark("test_q8")
    yield s
    s.stop()

def test_lower(spark):
    emp,_,country = get_dfs(spark)
    df = with_country(emp,country)
    assert "load_date" in lower_and_date(df).columns