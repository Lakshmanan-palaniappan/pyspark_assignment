from pyspark.sql import SparkSession
def get_spark(name):
    return SparkSession.builder.appName(name).getOrCreate()
def get_credit_card_dfs(spark):
    data = [
        ("1234567891234567",),
        ("5678912345671234",),
        ("9123456712345678",),
        ("1234567812341122",),
        ("1234567812341342",)
    ]
    df1 = spark.createDataFrame(data, ["card_number"])
    rdd = spark.sparkContext.parallelize(data)
    df2 = rdd.toDF(["card_number"])
    df3 = spark.read.json(
        spark.sparkContext.parallelize(
            ['{"card_number":"1234567891234567"}',
             '{"card_number":"5678912345671234"}',
             '{"card_number":"9123456712345678"}',
             '{"card_number":"1234567812341122"}',
             '{"card_number":"1234567812341342"}']
        )
    )
    return df1, df2, df3