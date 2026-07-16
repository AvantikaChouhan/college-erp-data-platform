import pandas as pd
import random

# -----------------------------
# Read Students CSV
# -----------------------------

students_df = pd.read_csv("students.csv")

placements = []

placement_id = 1

companies = [
    "TCS",
    "Infosys",
    "Wipro",
    "Accenture",
    "Capgemini",
    "Cognizant",
    "Amazon",
    "Microsoft"
]

# -----------------------------
# Generate Placements
# -----------------------------

for _, student in students_df.iterrows():

    if student["semester"] != 8:
        continue

    roll_no = student["roll_no"]

    placement_status = random.choice([
        "Placed",
        "Not Placed"
    ])

    if placement_status == "Placed":

        company = random.choice(companies)

        package_lpa = round(random.uniform(3, 15), 2)

    else:

        company = None

        package_lpa = None

    placement = {

        "placement_id": placement_id,

        "roll_no": roll_no,

        "company": company,

        "package_lpa": package_lpa,

        "placement_status": placement_status

    }

    placements.append(placement)

    placement_id += 1

# -----------------------------
# Save CSV
# -----------------------------

print("Total Placements:", len(placements))

placements_df = pd.DataFrame(placements)

placements_df.to_csv("placements.csv", index=False)

print("placements.csv created successfully!")