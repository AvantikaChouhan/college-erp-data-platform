import pandas as pd
import random

# -----------------------------
# Read Students CSV
# -----------------------------

students_df = pd.read_csv("students.csv")

fees = []

fee_id = 1

# -----------------------------
# Generate Fees
# -----------------------------

for _, student in students_df.iterrows():

    roll_no = student["roll_no"]
    semester = student["semester"]

    total_fee = 75000

    payment_status = random.choice([
        "Paid",
        "Partial",
        "Pending"
    ])

    if payment_status == "Paid":
        amount_paid = total_fee

    elif payment_status == "Partial":
        amount_paid = random.randint(20000, 70000)

    else:
        amount_paid = 0

    pending_amount = total_fee - amount_paid

    fee = {
        "fee_id": fee_id,
        "roll_no": roll_no,
        "semester": semester,
        "total_fee": total_fee,
        "amount_paid": amount_paid,
        "pending_amount": pending_amount,
        "payment_status": payment_status
    }

    fees.append(fee)

    fee_id += 1

# -----------------------------
# Save CSV
# -----------------------------

print("Total Fee Records:", len(fees))

fees_df = pd.DataFrame(fees)

fees_df.to_csv("fees.csv", index=False)

print("fees.csv created successfully!")