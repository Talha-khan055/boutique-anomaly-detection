
import pandas as pd
import random
from datetime import datetime, timedelta
import os

# Make random data repeatable
random.seed(42)

# Create transaction data
categories = ["Dresses", "Shoes", "Bags", "Jewelry", "Accessories"]

transactions = []

for i in range(1, 151):
    transaction_date = datetime(2026, 1, 1) + timedelta(
        days=random.randint(0, 300)
    )

    transaction = {
        "date": transaction_date.strftime("%Y-%m-%d"),
        "id": f"T{i:03d}",
        "amount": random.randint(500, 15000),
        "category": random.choice(categories),
        "customer_id": f"C{random.randint(1, 50):03d}"
    }

    transactions.append(transaction)

# Add a few unusual purchase amounts
transactions[10]["amount"] = 85000
transactions[40]["amount"] = 95000
transactions[90]["amount"] = 120000

# Create a DataFrame
df = pd.DataFrame(transactions)

# Save CSV inside the data folder
os.makedirs("data", exist_ok=True)
df.to_csv("data/transactions.csv", index=False)

print("150 transactions generated successfully!")
print(df.head())
