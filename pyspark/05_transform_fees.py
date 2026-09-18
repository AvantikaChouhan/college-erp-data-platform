from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, count

spark = SparkSession.builder \
    .appName("CollegeERP_Fees_Transformation") \
    .getOrCreate()

fees = spark.read.csv(
    "data/fees.csv",
    header=True,
    inferSchema=True
)

print("=== Fees Schema ===")
fees.printSchema()

print("=== Fees Data ===")
fees.show(10)

# Department information ke liye students data read karo
students = spark.read.csv(
    "data/students.csv",
    header=True,
    inferSchema=True
)

students_selected = students.select(
    "roll_no",
    "student_name",
    "department"
)

# JOIN
student_fees = students_selected.join(
    fees,
    on="roll_no",
    how="inner"
)

print("=== Student Fees After JOIN ===")

student_fees.show(10)

# Department-wise fee collection
department_fees = student_fees.groupBy(
    "department"
).agg(
    sum("amount_paid").alias("total_fees"),
    count("roll_no").alias("total_fee_records")
).orderBy(
    col("total_fees").desc()
)

print("=== Department-wise Fee Collection ===")

department_fees.show()

# Pending fees
pending_fees = student_fees.filter(
    col("payment_status") == "Pending"
)

print("=== Pending Fees ===")

pending_fees.show(10)

print(
    "Pending fee records:",
    pending_fees.count()
)

spark.stop()