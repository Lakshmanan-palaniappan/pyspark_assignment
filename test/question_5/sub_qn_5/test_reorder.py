import pytest
from src.question_5.sub_qn_1.util import get_spark, get_dfs
from src.question_5.sub_qn_5.util import reorder
@pytest.fixture(scope="session")
def spark():
    s = get_spark("test_q5")
    yield s
    s.stop()
def test_reorder(spark):
    emp,_,_ = get_dfs(spark)
    assert reorder(emp).columns[0] == "employee_id"