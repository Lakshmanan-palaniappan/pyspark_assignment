import pytest
from src.question_1.sub_qn_1.util import get_spark, get_purchase_df
from src.question_1.sub_qn_3.util import upgrade_to_iphone14
@pytest.fixture(scope="session")
def spark():
    spark = get_spark("test_upgrade")
    yield spark
    spark.stop()
def test_upgrade_count(spark):
    df = get_purchase_df(spark)
    result = upgrade_to_iphone14(df)
    assert result.count() == 2
def test_upgrade_values(spark):
    df = get_purchase_df(spark)
    result = sorted([row.customer for row in upgrade_to_iphone14(df).collect()])
    assert result == [1, 3]
def test_upgrade_columns(spark):
    df = get_purchase_df(spark)
    result = upgrade_to_iphone14(df)
    assert result.columns == ["customer", "upgraded", "products"]