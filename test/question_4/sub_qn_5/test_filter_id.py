import pytest
from src.question_4.sub_qn_1.util import get_spark, read_json
from src.question_4.sub_qn_5.util  import filter_id

@pytest.fixture(scope="session")
def spark():
    s = get_spark("test_q5")
    yield s
    s.stop()

def test_filter(spark):
    df = read_json(spark)
    assert filter_id(df).count() == 1