from src.question_5.sub_qn_1.util import get_spark, get_dfs
from src.question_5.sub_qn_7.util import with_country
from util import write_external_tables
spark = get_spark("q9")
emp, _, country = get_dfs(spark)
df = with_country(emp, country)
write_external_tables(df, spark)