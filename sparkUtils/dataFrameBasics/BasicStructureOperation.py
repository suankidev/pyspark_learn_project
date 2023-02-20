import pyspark.sql
from common_utils.sparkUtils import getSparkSession
from pyspark.sql.types import StructType,StructField,StringType,Row
from pyspark.sql.functions import col,column,expr,count,avg,sum,countDistinct

class BasicStructureOperaion:
    def df_basics(self,flightDf2015):
        source=col("source")
        print(type(source))

    def df_manual_creation(self,spark:pyspark.sql.SparkSession):
        test=Row(1,"hello",False,4,567.34973)
        print(test[0])

        myschema=StructType([StructField("name",StringType(),False),StructField("Age",StringType(),False)])
        names=[Row("sujeet","30"),Row("Ankita","24")]
        spark.createDataFrame(names,myschema).show()
        spark.createDataFrame(names,["name","age"]).show()
        spark.sparkContext.parallelize(names).toDF(["name","age"]).show()

    def df_expression(self,flightDF,spark:pyspark.sql.SparkSession):
        flightDF.select(col('*'),(col("source")==col("target")).alias("same"))\
            .where(col("same")==True).show()

        #flightDF.select(expr("source as origin"),col("target").alias("destination")).show()

        flightDF.select(avg(col("totalflight")),countDistinct(col("source"))).show()



def basic_structure_operation():
    spark=getSparkSession()
    file_path="C:\\Users\\sujee\\Desktop\\spark_input\\fligt_data\\2015*.csv"
    flight_schema=StructType([StructField("target",StringType(),False),
                              StructField("source",StringType(),False),
                              StructField("totalflight",StringType(),False,metadata={"hello":"world"})]
                             )
    flightData2015=spark.read.option("header","true").schema(flight_schema)\
    .format("csv").load(file_path)

    myobj=BasicStructureOperaion()

    #myobj.df_basics(flightData2015)
    #myobj.df_manual_creation(spark)
    myobj.df_expression(flightData2015,spark)