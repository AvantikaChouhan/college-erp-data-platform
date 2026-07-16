import pandas as pd
import random

# -----------------------------
# Read CSV Files
# -----------------------------

students_df = pd.read_csv("students.csv")
subjects_df = pd.read_csv("subjects.csv")

attendance = []

attendance_id = 1

# -----------------------------
# Generate Attendance
# -----------------------------

for _, student in students_df.iterrows():

    # Student Details
    roll_no = student["roll_no"]
    student_semester = student["semester"]

    # Get Subjects of Student's Semester
    semester_subjects = subjects_df[
    (subjects_df["semester"] == student_semester) &
    (subjects_df["department"] == student["department"])
]
    # Generate Attendance for Each Subject
    for _, subject in semester_subjects.iterrows():

        subject_code = subject["subject_code"]

        attendance_percentage = random.randint(40, 100)

        attendance_record = {
            "attendance_id": attendance_id,
            "roll_no": roll_no,
            "subject_code": subject_code,
            "attendance_percentage": attendance_percentage
        }

        attendance.append(attendance_record)

        attendance_id += 1

# -----------------------------
# Display Total Attendance Records
# -----------------------------

print("Total Attendance Records:", len(attendance))

# -----------------------------
# Create DataFrame
# -----------------------------

attendance_df = pd.DataFrame(attendance)

# -----------------------------
# Save CSV
# -----------------------------

attendance_df.to_csv("attendance.csv", index=False)

print("attendance.csv created successfully!")