# python
import findspark

from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession



# [opt] Create a variable with the absolute path to the text file 
logFile = "/home/workspace/Test.txt"

# create a Spark Session 
spark = SparkSession.builder \
    .master("local") \
    .appName("Spark") \
    .config("spark.sql.repl.eagerEval.enabled", True) \
    .getOrCreate()

# set the log level to WARN
spark.sparkContext.setLogLevel("WARN")

logData = spark.read.text(logFile).cache()
# write functions
df = spark.createDataFrame([('1', 100), ('2', 200), ('3', 300)]).toDF("id", "value")
df

# stop Spark
spark.stop()