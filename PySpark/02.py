from pyspark.sql import SparkSession
from pyspark.sql.functions import *

if __name__ == '__main__':
    spark = SparkSession \
        .builder \
        .master('local[*]') \
        .appName('Brojanje reci') \
        .getOrCreate()

    lines = spark.read.text('C:\\Users\\aleks\\PycharmProjects\\data\\PySpark\\source_data.csv')

    wordCounts = lines \
        .select(explode(split(lines.value, '\s+'))
                .alias('word')) \
        .groupby('word') \
        .count()

    print('\n Word Count: ', wordCounts.show(20, 5))

    spark.stop()
