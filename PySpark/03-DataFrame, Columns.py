from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Data Frame vezba').getOrCreate()

# read the dataset
df_pyspark = spark.read.csv('source_data.csv', header=True, inferSchema=True)
print(df_pyspark.show())

# check the schema
print(df_pyspark.printSchema())

# type of object
print(type(df_pyspark))

# column names
print(df_pyspark.columns)

# particular column(s)
print(df_pyspark.select(['name', 'age']).show())

# describe options
print(df_pyspark.describe().show())

# adding columns in pyspark df
print(df_pyspark.withColumn('experience', df_pyspark['age']-20).show())  # ovo nije INPLACE operacija

# drop column(s)
print(df_pyspark.drop('age').show())  # ovo nije INPLACE operacija

# rename the column
print(df_pyspark.withColumnRenamed('age', 'Age').show())
