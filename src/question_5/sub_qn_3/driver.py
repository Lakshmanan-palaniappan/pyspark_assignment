from src.question_5.sub_qn_1.util import get_spark, get_dfs
from util import filter_m
spark = get_spark("q3")
emp,dept,_ = get_dfs(spark)
filter_m(emp,dept).show()