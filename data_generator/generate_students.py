from faker import Faker
from config import departments, generate_phone, generate_email
import random
import pandas as pd

fake = Faker("en_IN")

students = []

# -----------------------------
# Generate One Student
# -----------------------------

def generate_student(student_number):

    # -----------------------------
    # Generate Student Name
    # -----------------------------
    name = fake.name()

    # -----------------------------
    # Generate Email
    # -----------------------------
    email = generate_email(name)

    # -----------------------------
    # Generate Phone
    # -----------------------------
    phone = generate_phone()

    # -----------------------------
    # Generate Department
    # -----------------------------
    department = random.choice(list(departments.keys()))
    department_id = departments[department]

    # -----------------------------
    # Generate Roll Number
    # -----------------------------
    roll_no = department + "24" + str(student_number).zfill(3)

    # -----------------------------
    # Generate Semester
    # -----------------------------
    semester = random.randint(1, 8)

    # -----------------------------
    # Generate Grade
    # -----------------------------
    grades = ["A+", "A", "B+", "B", "C"]
    grade = random.choice(grades)

    # -----------------------------
    # Generate Father Name
    # -----------------------------
    surname = name.split()[-1]
    father_name = fake.first_name_male() + " " + surname

    # -----------------------------
    # Create Student Dictionary
    # -----------------------------
    student = {
    "student_name": name,
    "student_contact": phone,
    "student_email": email,
    "roll_no": roll_no,
    "semester": semester,
    "department": department,
    "department_id": department_id,
    "grade": grade,
    "father_name": father_name
}

    return student


# -----------------------------
# Generate 500 Students
# -----------------------------

for i in range(500):
    student = generate_student(i + 1)
    students.append(student)

print("Total Students Generated:", len(students))

# -----------------------------
# Create DataFrame
# -----------------------------

students_df = pd.DataFrame(students)

# -----------------------------
# Save CSV
# -----------------------------

students_df.to_csv("students.csv", index=False)

print("students.csv created successfully!")