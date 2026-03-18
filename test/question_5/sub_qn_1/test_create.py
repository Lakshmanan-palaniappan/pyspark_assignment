import pytest
from src.question_5.sub_qn_1.util import get_spark, get_dfs
@pytest.fixture(scope="session")
def spark():
    s = get_spark("test_q1")
    yield s
    s.stop()
def test_counts(spark):
    emp, dept, country = get_dfs(spark)

    assert emp.count() == 7
    assert dept.count() == 5
    assert country.count() == 3
def test_columns(spark):
    emp, dept, country = get_dfs(spark)
    assert emp.columns == ["employee_id","employee_name","department","state","salary","age"]
    assert dept.columns == ["dept_id","dept_name"]
    assert country.columns == ["country_code","country_name"]
def test_data_sample(spark):
    emp, _, _ = get_dfs(spark)
    names = [r.employee_name for r in emp.collect()]
    assert "james" in names
    assert "maria" in names