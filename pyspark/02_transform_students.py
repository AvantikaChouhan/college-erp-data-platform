from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count

# Create Spark session
spark = SparkSession.builder \
    .appName("CollegeERP_Student_Transformation") \
    .getOrCreate()

# Read students data
df = spark.read.csv(
    "data/students.csv",
    header=True,
    inferSchema=True
)

# 1. Select required columns
students = df.select(
    "roll_no",
    "student_name",
    "department",
    "semester",
    "grade"
)

print("=== Selected Student Data ===")
students.show(10)

# 2. Filter CSE students
cse_students = students.filter(
    col("department") == "CSE"
)

print("=== CSE Students ===")
cse_students.show(10)

# 3. Department-wise student count
dept_count = students.groupBy(
    "department"
).agg(
    count("roll_no").alias("total_students")
).orderBy(
    col("total_students").desc()
)

print("=== Department-wise Student Count ===")
dept_count.show()

spark.stop()