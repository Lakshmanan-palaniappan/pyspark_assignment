import pytest
from src.question_2.sub_qn_1.util import get_spark, get_credit_card_dfs


@pytest.fixture(scope="session")
def spark():
    spark = get_spark("test")
    yield spark
    spark.stop()
def test_counts(spark):
    df1, df2, df3 = get_credit_card_dfs(spark)
    assert df1.count() == 5
    assert df2.count() == 5
    assert df3.count() == 5
def test_schema(spark):
    df1, df2, df3 = get_credit_card_dfs(spark)
    assert df1.columns == ["card_number"]
    assert df2.columns == ["card_number"]
    assert df3.columns == ["card_number"]