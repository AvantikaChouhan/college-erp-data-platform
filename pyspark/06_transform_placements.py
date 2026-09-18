from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, count, round

spark = SparkSession.builder \
    .appName("CollegeERP_Placements_Transformation") \
    .getOrCreate()

# Read students
students = spark.read.csv(
    "data/students.csv",
    header=True,
    inferSchema=True
)

# Read placements
placements = spark.read.csv(
    "data/placements.csv",
    header=True,
    inferSchema=True
)

print("=== Placements Schema ===")
placements.printSchema()

print("=== Placements Data ===")
placements.show(10)

# Select required student columns
students_selected = students.select(
    "roll_no",
    "student_name",
    "department"
)

# Select placement columns
placements_selected = placements.select(
    "roll_no",
    "company",
    "package_lpa"
)

# JOIN
student_placements = students_selected.join(
    placements_selected,
    on="roll_no",
    how="left"
)

print("=== Student Placements After JOIN ===")

student_placements.show(10)

# Placed students
placed_students = student_placements.filter(
    col("package_lpa") > 0
)

print("=== Placed Students ===")

placed_students.show(10)

print(
    "Total placed students:",
    placed_students.count()
)

# Department-wise placement analysis
department_placements = placed_students.groupBy(
    "department"
).agg(
    count("roll_no").alias("placed_students"),
    round(avg("package_lpa"), 2).alias("average_package_lpa")
).orderBy(
    col("placed_students").desc()
)

print("=== Department-wise Placement Analysis ===")

department_placements.show()

# Unplaced students
unplaced_students = student_placements.filter(
    col("package_lpa") == 0
)

print("=== Unplaced Students ===")

unplaced_students.show(10)

print(
    "Total unplaced students:",
    unplaced_students.count()
)

spark.stop()