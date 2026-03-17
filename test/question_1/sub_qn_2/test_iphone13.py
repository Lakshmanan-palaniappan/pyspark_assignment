import pytest
from src.question_1.sub_qn_1.util import get_spark, get_purchase_df
from src.question_1.sub_qn_2.util import only_iphone13
@pytest.fixture(scope="session")
def spark():
    spark = get_spark("test")
    yield spark
    spark.stop()
def test_only_iphone13_count(spark):
    df = get_purchase_df(spark)
    result = only_iphone13(df)
    assert result.count() == 1
def test_only_iphone13_value(spark):
    df = get_purchase_df(spark)
    result = [row.customer for row in only_iphone13(df).collect()]
    assert result == [4]
def test_only_iphone13_schema(spark):
    df = get_purchase_df(spark)
    result = only_iphone13(df)
    assert result.columns == ["customer"]