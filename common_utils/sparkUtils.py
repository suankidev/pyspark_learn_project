from pyspark.sql.session import SparkSession


def getSparkSession():
    spark=SparkSession.builder.master("local[2]") \
        .appName("sparkdemo").getOrCreate()
    return spark