from pyspark.sql import SparkSession
from pyspark.sql.functions import col, round

# PostgreSQL connection config
POSTGRES_URL = "jdbc:postgresql://postgres:5432/sparkdb"
POSTGRES_PROPERTIES = {
    "user": "sparkuser",
    "password": "sparkpass",
    "driver": "org.postgresql.Driver"
}

spark = SparkSession.builder \
    .appName("ETL to PostgreSQL") \
    .getOrCreate()

df = spark.read.csv("data/sales_data.csv", header=True, inferSchema=True)

df_transformed = df.withColumn("revenue", col("quantity") * col("unit_price")) \
    .withColumn("cost", col("quantity") * col("cost_price")) \
    .withColumn("profit", col("revenue") - col("cost")) \
    .withColumn("profit_margin", round((col("profit") / col("revenue")) * 100, 2))

df_transformed.show()
print(spark.sparkContext._conf.get("spark.jars"))
print("Spark JARs:", spark.sparkContext._conf.get("spark.jars"))


# Save to PostgreSQL
df_transformed.write.jdbc(url=POSTGRES_URL, table="sales", mode="append", properties=POSTGRES_PROPERTIES)

spark.stop()
