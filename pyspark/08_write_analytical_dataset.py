from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count, col, round, when


# =========================================================
# 1. CREATE SPARK SESSION
# =========================================================

spark = SparkSession.builder \
    .appName("CollegeERP_Write_Analytical_Dataset") \
    .config(
        "spark.hadoop.fs.file.impl",
        "org.apache.hadoop.fs.LocalFileSystem"
    ) \
    .getOrCreate()


# =========================================================
# 2. READ DATA
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
# 3. STUDENT MASTER
# =========================================================

student_master = students.select(
    "roll_no",
    "student_name",
    "department",
    "semester"
)


# =========================================================
# 4. ATTENDANCE SUMMARY
# =========================================================

attendance_summary = attendance.groupBy(
    "roll_no"
).agg(
    round(
        avg("attendance_percentage"),
        2
    ).alias("avg_attendance")
)


# =========================================================
# 5. RESULTS SUMMARY
# =========================================================

results_summary = results.groupBy(
    "roll_no"
).agg(
    round(
        avg("marks"),
        2
    ).alias("avg_marks"),
    count("subject_code").alias("total_subjects")
)


# =========================================================
# 6. FEES
# =========================================================

fees_selected = fees.select(
    "roll_no",
    "total_fee",
    "amount_paid",
    "pending_amount",
    "payment_status"
)


# =========================================================
# 7. PLACEMENTS
# =========================================================

placements_selected = placements.select(
    "roll_no",
    "company",
    "package_lpa",
    "placement_status"
)


# =========================================================
# 8. JOIN ALL DATA
# =========================================================

final_dataset = student_master \
    .join(
        attendance_summary,
        on="roll_no",
        how="left"
    ) \
    .join(
        results_summary,
        on="roll_no",
        how="left"
    ) \
    .join(
        fees_selected,
        on="roll_no",
        how="left"
    ) \
    .join(
        placements_selected,
        on="roll_no",
        how="left"
    )


# =========================================================
# 9. HANDLE NULL PLACEMENT VALUES
# =========================================================

final_dataset = final_dataset.withColumn(
    "company",
    when(
        col("company").isNull(),
        "N/A"
    ).otherwise(
        col("company")
    )
)

final_dataset = final_dataset.withColumn(
    "package_lpa",
    when(
        col("package_lpa").isNull(),
        0.0
    ).otherwise(
        col("package_lpa")
    )
)

final_dataset = final_dataset.withColumn(
    "placement_status",
    when(
        col("placement_status").isNull(),
        "Not Placed"
    ).otherwise(
        col("placement_status")
    )
)


# =========================================================
# 10. CONVERT SPARK DATAFRAME TO PANDAS
# =========================================================

final_pandas = final_dataset.toPandas()


# =========================================================
# 11. WRITE FINAL DATASET AS CSV
# =========================================================

output_file = "data/processed/student_analytics.csv"

final_pandas.to_csv(
    output_file,
    index=False
)


# =========================================================
# 12. VERIFICATION
# =========================================================

print("==========================================")
print("DATASET WRITTEN SUCCESSFULLY")
print("==========================================")

print(
    "Total Records:",
    len(final_pandas)
)

print(
    "Output File:",
    output_file
)

print("==========================================")


# =========================================================
# 13. STOP SPARK
# =========================================================

spark.stop()