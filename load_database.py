
import pandas as pd
import sqlite3
from pathlib import Path

# Find the project folder
BASE_DIR = Path(__file__).resolve().parent

# File locations
CSV_FILE = BASE_DIR / "data" / "transactions.csv"
DB_FILE = BASE_DIR / "data" / "boutique.db"

# Load CSV data
df = pd.read_csv(CSV_FILE)

# Connect to SQLite database
connection = sqlite3.connect(DB_FILE)

# Store data in a database table
df.to_sql(
    "transactions",
    connection,
    if_exists="replace",
    index=False
)

# Check how many records were inserted
cursor = connection.cursor()
cursor.execute("SELECT COUNT(*) FROM transactions")
total = cursor.fetchone()[0]

print("Database created successfully!")
print("Total records inserted:", total)
print("Database location:", DB_FILE)

# Close database connection
connection.close()
