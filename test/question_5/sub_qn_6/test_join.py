import pytest
from src.question_5.sub_qn_1.util import get_spark, get_dfs
from src.question_5.sub_qn_6.util import joins
@pytest.fixture(scope="session")
def spark():
    s = get_spark("test_q6")
    yield s
    s.stop()
def test_join(spark):
    emp,dept,_ = get_dfs(spark)
    assert joins(emp,dept).count() > 0