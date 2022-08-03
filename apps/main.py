import pyspark.sql.functions as f
from pyspark.sql.types import *
from pyspark.sql import SparkSession
import os


def spark_init():
    spark = SparkSession \
        .builder \
        .appName("spark_cron") \
        .master("local[5]") \
        .getOrCreate()
    return spark


if __name__ == "__main__":

    spark = spark_init()

    extract_df = spark.read.format("json").load("/opt/spark/work-dir/apps/yelp_academic_dataset_tip.json")
    extract_df.printSchema()

    extract_df.write.format('jdbc').options(  
        url=f'jdbc:mysql://10.100.106.152:3306/de_sandbox',
        driver='com.mysql.jdbc.Driver',
        dbtable='spark_poc',
        user=os.getenv("MYSQL_USERNAME"),
        password=os.getenv("MYSQL_PASSWORD")).mode('append').save()