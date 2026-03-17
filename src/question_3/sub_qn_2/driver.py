from src.question_3.sub_qn_1.util import get_spark, get_df
from util import rename_cols
spark = get_spark("q2")
df = rename_cols(get_df(spark))
df.show()