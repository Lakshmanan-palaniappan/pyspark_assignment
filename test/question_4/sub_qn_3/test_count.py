import pytest
from src.question_4.sub_qn_1.util import get_spark, read_json
from src.question_4.sub_qn_2.util import flatten
from src.question_4.sub_qn_3.util  import count_diff
@pytest.fixture(scope="session")
def spark():
    s = get_spark("test_q3")
    yield s
    s.stop()
def test_counts(spark):
    df = read_json(spark)
    flat = flatten(df)
    orig, new = count_diff(df, flat)
    assert orig == 1
    assert new == 3