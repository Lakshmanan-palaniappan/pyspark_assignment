import pytest
from src.question_4.sub_qn_1.util import get_spark, read_json
@pytest.fixture(scope="session")
def spark():
    s = get_spark("test")
    yield s
    s.stop()
def test_read(spark):
    df = read_json(spark)
    assert df.count() >= 1