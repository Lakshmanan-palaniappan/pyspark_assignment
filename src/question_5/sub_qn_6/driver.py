from src.question_5.sub_qn_1.util import get_spark, get_dfs
from util import joins
spark = get_spark("q6")
emp,dept,_ = get_dfs(spark)
joins(emp,dept).show()