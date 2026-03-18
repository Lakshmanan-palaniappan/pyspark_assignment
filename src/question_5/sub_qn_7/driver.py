from src.question_5.sub_qn_1.util import get_spark, get_dfs
from util import with_country
spark = get_spark("q7")
emp,_,country = get_dfs(spark)
with_country(emp,country).show()