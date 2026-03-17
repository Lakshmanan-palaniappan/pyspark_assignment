from src.question_1.sub_qn_1.util import *
from util import new_products

spark=get_spark("new_prods")
pur_df=get_purchase_df(spark)
prod_df=get_product_df(spark)
new_products(prod_df,pur_df).show(truncate=False)