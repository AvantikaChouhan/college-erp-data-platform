from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, count, round

spark = SparkSession.builder \
    .appName("CollegeERP_Results_Transformation") \
    .getOrCreate()

# Read students
students = spark.read.csv(
    "data/students.csv",
    header=True,
    inferSchema=True
)

# Read results
results = spark.read.csv(
    "data/results.csv",
    header=True,
    inferSchema=True
)

print("=== Results Schema ===")
results.printSchema()

print("=== Results Data ===")
results.show(10)

# Select only required columns BEFORE JOIN
students_selected = students.select(
    "roll_no",
    "student_name",
    "department",
    "semester"
)

results_selected = results.select(
    "roll_no",
    "subject_code",
    "marks",
    col("grade").alias("result_grade"),
    "result_status"
)

# JOIN
student_results = students_selected.join(
    results_selected,
    on="roll_no",
    how="inner"
)

print("=== Student Results After JOIN ===")

student_results.select(
    "roll_no",
    "student_name",
    "department",
    "semester",
    "subject_code",
    "marks",
    "result_grade",
    "result_status"
).show(10)

# Department-wise average marks
department_results = student_results.groupBy(
    "department"
).agg(
    round(avg("marks"), 2).alias("average_marks"),
    count("roll_no").alias("total_result_records")
).orderBy(
    col("average_marks").desc()
)

print("=== Department-wise Result Analysis ===")
department_results.show()

# Low-performing records
low_performers = student_results.filter(
    col("marks") < 50
)

print("=== Low Performing Result Records ===")

low_performers.select(
    "roll_no",
    "student_name",
    "department",
    "subject_code",
    "marks",
    "result_grade",
    "result_status"
).show(10)

print(
    "Low performing records:",
    low_performers.count()
)

spark.stop()