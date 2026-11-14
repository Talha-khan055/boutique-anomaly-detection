import pandas as pd

# Load transaction data
df = pd.read_csv("data/transactions.csv")

# Display the first five transactions
print("First five transactions:")
print(df.head())