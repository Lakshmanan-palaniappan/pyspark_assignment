from pyspark.sql import SparkSession

def get_spark(name):
    return SparkSession.builder.appName(name).getOrCreate()

def get_dfs(spark):
    emp = spark.createDataFrame([
        (11,"james","D101","ny",9000,34),
        (12,"michel","D101","ny",8900,32),
        (13,"robert","D102","ca",7900,29),
        (14,"scott","D103","ca",8000,36),
        (15,"jen","D102","ny",9500,38),
        (16,"jeff","D103","uk",9100,35),
        (17,"maria","D101","ny",7900,40)
    ], ["employee_id","employee_name","department","state","salary","age"])

    dept = spark.createDataFrame([
        ("D101","sales"),("D102","finance"),
        ("D103","marketing"),("D104","hr"),("D105","support")
    ], ["dept_id","dept_name"])

    country = spark.createDataFrame([
        ("ny","newyork"),("ca","California"),("uk","Russia")
    ], ["country_code","country_name"])

    return emp, dept, country