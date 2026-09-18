from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count, col, round

# Create Spark session
spark = SparkSession.builder \
    .appName("CollegeERP_Attendance_Transformation") \
    .getOrCreate()

# Read attendance data
attendance = spark.read.csv(
    "data/attendance.csv",
    header=True,
    inferSchema=True
)

print("=== Attendance Schema ===")
attendance.printSchema()

print("=== Attendance Data ===")
attendance.show(10)

# 1. Average attendance percentage for each student
student_attendance = attendance.groupBy(
    "roll_no"
).agg(
    round(avg("attendance_percentage"), 2).alias("avg_attendance")
)

print("=== Student Average Attendance ===")
student_attendance.show(10)

# 2. Students with attendance below 75%
low_attendance = student_attendance.filter(
    col("avg_attendance") < 75
)

print("=== Students Below 75% Attendance ===")
low_attendance.show(10)

print(
    "Students below 75%:",
    low_attendance.count()
)

# 3. Department-wise attendance
students = spark.read.csv(
    "data/students.csv",
    header=True,
    inferSchema=True
)

department_attendance = student_attendance.join(
    students.select("roll_no", "department"),
    on="roll_no",
    how="inner"
).groupBy(
    "department"
).agg(
    round(avg("avg_attendance"), 2).alias("department_avg_attendance")
).orderBy(
    col("department_avg_attendance").desc()
)

print("=== Department-wise Average Attendance ===")
department_attendance.show()

spark.stop()