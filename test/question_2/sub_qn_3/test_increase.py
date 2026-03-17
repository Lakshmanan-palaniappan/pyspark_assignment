import pytest
from src.question_2.sub_qn_1.util import get_spark, get_credit_card_dfs
from src.question_2.sub_qn_3.util  import increase
@pytest.fixture(scope="session")
def spark():
    spark = get_spark("test")
    yield spark
    spark.stop()
def test_increase(spark):
    df, _, _ = get_credit_card_dfs(spark)
    assert increase(df).rdd.getNumPartitions() == 5