import pytest
from src.question_1.sub_qn_1.util import get_spark, get_purchase_df, get_product_df

@pytest.fixture(scope="module")
def spark():
    spark = get_spark("test")
    yield spark
    spark.stop()

def test_purchase_count(spark):
    df = get_purchase_df(spark)
    assert df.count() == 11

def test_product_count(spark):
    df = get_product_df(spark)
    assert df.count() == 5

def test_columns(spark):
    df = get_purchase_df(spark)
    assert df.columns == ["customer", "product_model"]
