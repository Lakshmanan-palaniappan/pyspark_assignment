import pytest
from src.question_1.sub_qn_1.util import get_spark, get_purchase_df, get_product_df
from src.question_1.sub_qn_4.util import new_products
@pytest.fixture(scope="session")
def spark():
    spark = get_spark("test_new_products")
    yield spark
    spark.stop()
def test_new_products_count(spark):
    pur_df = get_purchase_df(spark)
    prod_df = get_product_df(spark)
    result = new_products(prod_df, pur_df)
    assert result.count() == 1
def test_new_products_value(spark):
    pur_df = get_purchase_df(spark)
    prod_df = get_product_df(spark)
    result = [row.customer for row in new_products(prod_df, pur_df).collect()]
    assert result == [1]
def test_new_products_schema(spark):
    pur_df = get_purchase_df(spark)
    prod_df = get_product_df(spark)
    result = new_products(prod_df, pur_df)
    assert result.columns == ["customer"]