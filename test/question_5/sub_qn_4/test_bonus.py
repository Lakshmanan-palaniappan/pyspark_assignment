import pytest
from src.question_5.sub_qn_1.util import get_spark, get_dfs
from src.question_5.sub_qn_4.util import add_bonus
@pytest.fixture(scope="session")
def spark():
    s = get_spark("test_q4")
    yield s
    s.stop()
def test_bonus(spark):
    emp,_,_ = get_dfs(spark)
    assert "bonus" in add_bonus(emp).columns