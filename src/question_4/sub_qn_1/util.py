from pyspark.sql import SparkSession
import os
def get_spark(name):
    return SparkSession.builder.appName(name).getOrCreate()
def read_json(spark):
    path = os.path.join(os.path.dirname(__file__), "..", "input.json")
    return spark.read.option("multiline", True).json(path)