import pytest
from src.question_2.sub_qn_1.util import get_spark, get_credit_card_dfs
from src.question_2.sub_qn_5.util  import mask_df

@pytest.fixture(scope="session")
def spark():
    spark = get_spark("test")
    yield spark
    spark.stop()
def test_mask_count(spark):
    df, _, _ = get_credit_card_dfs(spark)
    assert mask_df(df).count() == 5
def test_mask_value(spark):
    df, _, _ = get_credit_card_dfs(spark)
    vals = [r.masked_card_number for r in mask_df(df).collect()]
    assert "************4567" in vals
def test_mask_schema(spark):
    df, _, _ = get_credit_card_dfs(spark)
    assert mask_df(df).columns == ["card_number", "masked_card_number"]