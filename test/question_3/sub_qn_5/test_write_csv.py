import pytest
from src.question_3.sub_qn_1.util import get_spark, get_df
from src.question_3.sub_qn_2.util import rename_cols
from src.question_3.sub_qn_5.util  import write_csv
@pytest.fixture(scope="session")
def spark():
    s = get_spark("test_q5")
    yield s
    s.stop()
def test_write_csv(spark, tmp_path):
    df = rename_cols(get_df(spark))
    path = tmp_path / "csv_out"
    write_csv(df, str(path))
    assert path.exists()