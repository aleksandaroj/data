import pandas as pd
from pyspark.sql import SparkSession

v = pd.read_csv('source_data.csv')

print(v)


spark = SparkSession.builder.appName('Vezba').getOrCreate()

print(spark)

df_pyspark = spark.read.option('header', 'true').csv('source_data.csv')
print(type(df_pyspark))
print(df_pyspark.head(1))
print(df_pyspark.printSchema())
