from src.question_3.sub_qn_1.util import get_spark, get_df
from src.question_3.sub_qn_2.util import rename_cols
from util import write_csv
spark = get_spark("q5")
df = rename_cols(get_df(spark))
write_csv(df, "output/csv_data")