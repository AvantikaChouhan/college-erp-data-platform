import pandas as pd
import random

# -----------------------------
# Read CSV Files
# -----------------------------

students_df = pd.read_csv("students.csv")
subjects_df = pd.read_csv("subjects.csv")

results = []

result_id = 1

# -----------------------------
# Generate Results
# -----------------------------

for _, student in students_df.iterrows():

    # Student Details
    roll_no = student["roll_no"]
    student_semester = student["semester"]
    department = student["department"]

    # Get Subjects of Student's Semester and Department
    semester_subjects = subjects_df[
        (subjects_df["semester"] == student_semester) &
        (subjects_df["department"] == department)
    ]

    # -----------------------------
    # Decide Student Performance
    # -----------------------------

    performance = random.choice([
        "Excellent",
        "Good",
        "Average",
        "Weak",
        "Fail"
    ])

    # -----------------------------
    # Generate Result for Each Subject
    # -----------------------------

    for _, subject in semester_subjects.iterrows():

        subject_code = subject["subject_code"]

        # -----------------------------
        # Generate Marks
        # -----------------------------

        if performance == "Excellent":
            marks = random.randint(85, 100)

        elif performance == "Good":
            marks = random.randint(70, 84)

        elif performance == "Average":
            marks = random.randint(50, 69)

        elif performance == "Weak":
            marks = random.randint(35, 49)

        else:
            marks = random.randint(0, 34)

        # -----------------------------
        # Generate Grade
        # -----------------------------

        if marks >= 90:
            grade = "A+"

        elif marks >= 80:
            grade = "A"

        elif marks >= 70:
            grade = "B+"

        elif marks >= 60:
            grade = "B"

        elif marks >= 50:
            grade = "C"

        elif marks >= 35:
            grade = "D"

        else:
            grade = "F"

        # -----------------------------
        # Result Status
        # -----------------------------

        if marks >= 35:
            result_status = "Pass"
        else:
            result_status = "Fail"

        # -----------------------------
        # Create Result Dictionary
        # -----------------------------

        result = {
            "result_id": result_id,
            "roll_no": roll_no,
            "subject_code": subject_code,
            "marks": marks,
            "grade": grade,
            "result_status": result_status
        }

        # Add Result
        results.append(result)

        # Increment Result ID
        result_id += 1

# -----------------------------
# Display Total Results
# -----------------------------

print("Total Results Generated:", len(results))

# -----------------------------
# Create DataFrame
# -----------------------------

results_df = pd.DataFrame(results)

# -----------------------------
# Save CSV
# -----------------------------

results_df.to_csv("results.csv", index=False)

print("results.csv created successfully!")