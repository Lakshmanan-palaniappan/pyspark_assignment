from src.question_3.sub_qn_1.util import get_spark, get_df
from src.question_3.sub_qn_2.util import rename_cols
from util import write_table
spark = get_spark("q6")
spark.sql("CREATE DATABASE IF NOT EXISTS user")
df = rename_cols(get_df(spark))
write_table(df)