import pytest
from src.question_5.sub_qn_1.util import get_spark, get_dfs
from src.question_5.sub_qn_3.util import filter_m
@pytest.fixture(scope="session")
def spark():
    s = get_spark("test_q3")
    yield s
    s.stop()

def test_filter(spark):
    emp,dept,_ = get_dfs(spark)
    assert filter_m(emp,dept).count() == 2