from src.question_4.sub_qn_1.util import get_spark, read_json
from src.question_4.sub_qn_2.util import flatten
from util import count_diff
spark = get_spark("q3")
df = read_json(spark)
flat_df = flatten(df)
print(count_diff(df, flat_df))