from src.question_4.sub_qn_6.util import camel_to_snake
def test_convert():
    assert camel_to_snake("storeSize") == "store_size"