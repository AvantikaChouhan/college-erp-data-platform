from faker import Faker
from config import departments, generate_phone, generate_email
import random
import pandas as pd

fake = Faker("en_IN")

faculty = []

# -----------------------------
# Generate One Faculty
# -----------------------------

def generate_faculty(department, position):

    # Generate Faculty Name
    name = fake.name()

    # Generate Email
    email = generate_email(name)

    # Generate Phone
    phone = generate_phone()

    # Department ID
    department_id = departments[department]

    # Generate Salary
    if position == "HOD":
        salary = random.randint(120000, 150000)

    elif position == "Professor":
        salary = random.randint(90000, 120000)

    elif position == "Associate Professor":
        salary = random.randint(70000, 90000)

    else:
        salary = random.randint(50000, 70000)

    # Generate DOB
    dob = fake.date_of_birth(minimum_age=28, maximum_age=65)

    # Generate Gender
    gender = random.choice(["Male", "Female"])

    # Generate Address
    address = fake.address().replace("\n", ", ")

    # Create Faculty Dictionary
    faculty_member = {
    "faculty_name": name,
    "faculty_contact": phone,
    "faculty_email": email,
    "department": department,
    "department_id": department_id,
    "position": position,
    "salary": salary,
    "dob": dob,
    "gender": gender,
    "address": address
}
    return faculty_member


# -----------------------------
# Generate Faculty Data
# -----------------------------

for department in departments.keys():

    # 1 HOD
    faculty.append(generate_faculty(department, "HOD"))

    # 2 Professors
    for _ in range(2):
        faculty.append(generate_faculty(department, "Professor"))

    # 4 Associate Professors
    for _ in range(4):
        faculty.append(generate_faculty(department, "Associate Professor"))

    # 13 Assistant Professors
    for _ in range(13):
        faculty.append(generate_faculty(department, "Assistant Professor"))

# -----------------------------
# Display Total Faculty
# -----------------------------

print("Total Faculty Generated:", len(faculty))

# -----------------------------
# Create DataFrame
# -----------------------------

faculty_df = pd.DataFrame(faculty)

# -----------------------------
# Save CSV
# -----------------------------

faculty_df.to_csv("faculty.csv", index=False)

print("faculty.csv created successfully!")