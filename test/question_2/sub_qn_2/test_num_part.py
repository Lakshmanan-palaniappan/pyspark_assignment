import pytest
from src.question_2.sub_qn_1.util import get_spark, get_credit_card_dfs
from src.question_2.sub_qn_2.util import num_part
@pytest.fixture(scope="session")
def spark():
    spark = get_spark("test")
    yield spark
    spark.stop()

def test_partitions(spark):
    df, _, _ = get_credit_card_dfs(spark)
    assert num_part(df) >= 1