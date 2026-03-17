import pytest
from src.question_2.sub_qn_1.util import get_spark, get_credit_card_dfs
from src.question_2.sub_qn_4.util import decrease
@pytest.fixture(scope="session")
def spark():
    spark = get_spark("test")
    yield spark
    spark.stop()
def test_decrease(spark):
    df, _, _ = get_credit_card_dfs(spark)
    orig = df.rdd.getNumPartitions()
    df2 = df.repartition(5)
    df3 = decrease(df2, orig)
    assert df3.rdd.getNumPartitions() == 5