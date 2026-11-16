
import sqlite3
import pandas as pd
from pathlib import Path

# Find project files
BASE_DIR = Path(__file__).resolve().parent
DB_FILE = BASE_DIR / "data" / "boutique.db"
SQL_FILE = BASE_DIR / "sql" / "business_questions.sql"

# Connect to database
connection = sqlite3.connect(DB_FILE)

# Read SQL queries
with open(SQL_FILE, "r", encoding="utf-8") as file:
    sql_script = file.read()

# Separate the three queries
queries = sql_script.split(";")

# Execute and display each query
for number, query in enumerate(queries, start=1):
    if query.strip():
        print("\n" + "=" * 50)
        print(f"BUSINESS QUESTION {number}")
        print("=" * 50)

        result = pd.read_sql_query(query, connection)
        print(result.to_string(index=False))

# Close connection
connection.close()
