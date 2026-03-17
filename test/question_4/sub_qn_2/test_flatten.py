import pytest
from src.question_4.sub_qn_1.util import get_spark, read_json
from src.question_4.sub_qn_2.util import flatten
@pytest.fixture(scope="session")
def spark():
    s = get_spark("test_q2")
    yield s
    s.stop()

def test_flatten_count(spark):
    df = read_json(spark)
    flat = flatten(df)
    assert flat.count() == 3