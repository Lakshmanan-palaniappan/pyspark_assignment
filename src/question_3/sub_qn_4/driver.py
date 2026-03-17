from src.question_3.sub_qn_1.util import get_spark, get_df
from src.question_3.sub_qn_2.util import rename_cols
from util import add_login_date
spark = get_spark("q4")
df = rename_cols(get_df(spark))
add_login_date(df).show()