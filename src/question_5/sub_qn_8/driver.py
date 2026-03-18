from src.question_5.sub_qn_1.util import get_spark, get_dfs
from src.question_5.sub_qn_7.util import with_country
from util import lower_and_date
spark = get_spark("q8")
emp,_,country = get_dfs(spark)
df = with_country(emp,country)
lower_and_date(df).show()