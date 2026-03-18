from src.question_5.sub_qn_1.util import get_spark, get_dfs
from util import avg_salary
spark = get_spark("q2")
emp,_,_ = get_dfs(spark)
avg_salary(emp).show()