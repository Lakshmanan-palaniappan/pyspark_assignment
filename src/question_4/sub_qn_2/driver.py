from src.question_4.sub_qn_1.util import get_spark, read_json
from util import flatten
spark = get_spark("q2")
df = read_json(spark)
flatten(df).show(truncate=False)