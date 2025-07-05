from pyspark.sql import SparkSession
from pyspark.sql.functions import col, round

# Initialize Spark
spark = SparkSession.builder \
    .appName("Simple ETL") \
    .getOrCreate()

# Load CSV
df = spark.read.csv("../data/sales_data.csv", header=True, inferSchema=True)

# Transformation
df_transformed = df.withColumn("revenue", col("quantity") * col("unit_price")) \
                   .withColumn("cost", col("quantity") * col("cost_price")) \
                   .withColumn("profit", col("revenue") - col("cost")) \
                   .withColumn("profit_margin", round((col("profit") / col("revenue")) * 100, 2))

# Show result
df_transformed.show()

# TODO: Load into PostgreSQL (in later steps)

spark.stop()
