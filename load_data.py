
from pathlib import Path
import pandas as pd

# Find the project folder automatically
project_folder = Path(__file__).resolve().parent

# Load transaction data
file_path = project_folder / "data" / "transactions.csv"
df = pd.read_csv(file_path)

# Display the first five transactions
print("First five transactions:")
print(df.head())
