import pytest
from src.question_5.sub_qn_1.util import get_spark, get_dfs
from src.question_5.sub_qn_7.util import with_country
@pytest.fixture(scope="session")
def spark():
    s = get_spark("test_q7")
    yield s
    s.stop()
def test_country(spark):
    emp,_,country = get_dfs(spark)
    assert with_country(emp,country).count() > 0