from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count, sum, col, round, when

spark = SparkSession.builder \
    .appName("CollegeERP_Final_Analytical_Dataset") \
    .getOrCreate()

# =========================================================
# 1. READ DATASETS
# =========================================================

students = spark.read.csv(
    "data/students.csv",
    header=True,
    inferSchema=True
)

attendance = spark.read.csv(
    "data/attendance.csv",
    header=True,
    inferSchema=True
)

results = spark.read.csv(
    "data/results.csv",
    header=True,
    inferSchema=True
)

fees = spark.read.csv(
    "data/fees.csv",
    header=True,
    inferSchema=True
)

placements = spark.read.csv(
    "data/placements.csv",
    header=True,
    inferSchema=True
)

# =========================================================
# 2. STUDENT MASTER DATA
# =========================================================

student_master = students.select(
    "roll_no",
    "student_name",
    "department",
    "semester"
)

# =========================================================
# 3. ATTENDANCE SUMMARY
# =========================================================

attendance_summary = attendance.groupBy(
    "roll_no"
).agg(
    round(avg("attendance_percentage"), 2).alias("avg_attendance")
)

# =========================================================
# 4. RESULTS SUMMARY
# =========================================================

results_summary = results.groupBy(
    "roll_no"
).agg(
    round(avg("marks"), 2).alias("avg_marks"),
    count("subject_code").alias("total_subjects")
)

# =========================================================
# 5. FEES DATA
# =========================================================

fees_selected = fees.select(
    "roll_no",
    "total_fee",
    "amount_paid",
    "pending_amount",
    "payment_status"
)

# =========================================================
# 6. PLACEMENT DATA
# =========================================================

placements_selected = placements.select(
    "roll_no",
    "company",
    "package_lpa",
    "placement_status"
)

# =========================================================
# 7. JOIN ALL DATASETS
# =========================================================

final_dataset = student_master \
    .join(attendance_summary, on="roll_no", how="left") \
    .join(results_summary, on="roll_no", how="left") \
    .join(fees_selected, on="roll_no", how="left") \
    .join(placements_selected, on="roll_no", how="left")

# =========================================================
# 8. HANDLE MISSING PLACEMENT VALUES
# =========================================================

final_dataset = final_dataset.withColumn(
    "company",
    when(
        col("company").isNull(),
        "N/A"
    ).otherwise(col("company"))
)

final_dataset = final_dataset.withColumn(
    "package_lpa",
    when(
        col("package_lpa").isNull(),
        0.0
    ).otherwise(col("package_lpa"))
)

final_dataset = final_dataset.withColumn(
    "placement_status",
    when(
        col("placement_status").isNull(),
        "Not Placed"
    ).otherwise(col("placement_status"))
)

# =========================================================
# 9. DISPLAY FINAL DATASET
# =========================================================

print("=== FINAL ANALYTICAL DATASET ===")

final_dataset.show(10)

print("=== FINAL SCHEMA ===")

final_dataset.printSchema()

print(
    "Total Students in Final Dataset:",
    final_dataset.count()
)

# =========================================================
# 10. FINAL DATASET SUMMARY
# =========================================================

print("=== FINAL DATASET SUMMARY ===")

final_dataset.select(
    "roll_no",
    "student_name",
    "department",
    "semester",
    "avg_attendance",
    "avg_marks",
    "total_subjects",
    "total_fee",
    "amount_paid",
    "pending_amount",
    "payment_status",
    "company",
    "package_lpa",
    "placement_status"
).show(10)

spark.stop()