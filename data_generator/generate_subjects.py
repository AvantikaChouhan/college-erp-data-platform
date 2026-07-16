from config import departments, subjects
import pandas as pd

subjects_list = []

subject_id = 1

# -----------------------------
# Generate Subjects
# -----------------------------

for department in departments.keys():

    department_id = departments[department]

    semester_subject_number = 1
    current_semester = 1

    # Loop through all subjects
    for subject_name, semester in subjects[department]:

        # Reset numbering when semester changes
        if semester != current_semester:
            current_semester = semester
            semester_subject_number = 1

        # Generate Subject Code
        subject_code = (
            department
            + str(semester)
            + str(semester_subject_number).zfill(2)
        )

        credits = 4

        subject = {
            "subject_id": subject_id,
            "subject_name": subject_name,
            "subject_code": subject_code,
            "department_id": department_id,
            "department": department,
            "semester": semester,
            "credits": credits
        }

        subjects_list.append(subject)

        subject_id += 1
        semester_subject_number += 1

# -----------------------------
# Display Total Subjects
# -----------------------------

print("Total Subjects Generated:", len(subjects_list))

# -----------------------------
# Create DataFrame
# -----------------------------

subjects_df = pd.DataFrame(subjects_list)

# -----------------------------
# Save CSV
# -----------------------------

subjects_df.to_csv("subjects.csv", index=False)

print("subjects.csv created successfully!")