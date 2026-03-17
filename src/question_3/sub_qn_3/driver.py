from src.question_3.sub_qn_1.util import get_spark, get_df
from src.question_3.sub_qn_2.util  import rename_cols
from util import last_7_days
spark = get_spark("q3")
df = rename_cols(get_df(spark))
last_7_days(df).show()