import pytest
from src.question_5.sub_qn_1.util import get_spark, get_dfs
from src.question_5.sub_qn_2.util import avg_salary
@pytest.fixture(scope="session")
def spark():
    s = get_spark("test_q2")
    yield s
    s.stop()
def test_avg(spark):
    emp,_,_ = get_dfs(spark)
    assert avg_salary(emp).count() > 0