from faker import Faker
from config import departments
import random
import pandas as pd

fake = Faker('en_IN')

students = []

# -----------------------------
# Generate One Student
# -----------------------------

def generate_student(student_number):

    # Generate Student Name
    name = fake.name()

    # Generate Email
    email = (
        name.lower()
            .replace(" ", ".")
            + "@gmail.com"
    )

    # Generate Indian Mobile Number

    # First digit can be 7, 8 or 9
    first_digit = str(random.choice([7, 8, 9]))

    # Store remaining 9 digits
    remaining_digits = ""

    # Generate remaining digits
    for i in range(9):
        remaining_digits += str(random.randint(0, 9))

    # Combine first digit and remaining digits
    phone = first_digit + remaining_digits

    
    # Select a random department
    department = random.choice(list(departments.keys()))

    # Get corresponding department ID
    department_id = departments[department]

    # Generate Roll Number
    roll_number = department + "24" + str(student_number).zfill(3)

    # Generate Semester
    semester = random.randint(1, 8)

    # Generate Grade
    grades = ["A+", "A", "B+", "B", "C"]
    grade = random.choice(grades)

    # Generate Father Name
    name_parts = name.split()
    surname = name_parts[-1]

    father_first_name = fake.first_name_male()
    father_name = father_first_name + " " + surname

    # Create Student Dictionary
    student = {
    "student_name": name,
    "student_contact": phone,
    "student_email": email,
    "roll_no": roll_number,
    "semester": semester,
    "department_id": department_id,
    "grade": grade,
    "father_name": father_name
}

    return student


# -----------------------------
# Generate One Student (Testing)
# -----------------------------

# student = generate_student(1)

# print("Student Name    :", student["student_name"])
# print("Student Contact :", student["student_contact"])
# print("Student Email   :", student["student_email"])
# print("Roll Number     :", student["roll_no"])
# print("Semester        :", student["semester"])
# print("Department ID   :", student["department_id"])
# print("Grade           :", student["grade"])
# print("Father Name     :", student["father_name"])

# -----------------------------
# Generate 500 Students
# -----------------------------

for i in range(500):
    student = generate_student(i + 1)
    students.append(student)

print("Total Students Generated:", len(students))