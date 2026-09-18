from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("CollegeERP") \
    .getOrCreate()

# Read students CSV
df = spark.read.csv(
    "data/students.csv",
    header=True,
    inferSchema=True
)

# Display data
df.show()

# Display schema
df.printSchema()

# Total records
print("Total Students:", df.count())

spark.stop()