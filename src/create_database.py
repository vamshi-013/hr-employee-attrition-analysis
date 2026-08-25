import pandas as pd
import sqlite3
import os

# Load dataset
df = pd.read_csv("data/hr_employee_attrition.csv")

print("Dataset loaded successfully!")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")

# Create database folder
os.makedirs("database", exist_ok=True)

# Database path
db_path = "database/hr_employee_attrition.db"

# Connect to SQLite
conn = sqlite3.connect(db_path)

# Save dataframe to database
df.to_sql(
    "employees",
    conn,
    if_exists="replace",
    index=False
)

# Verify row count
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM employees")

total_rows = cursor.fetchone()[0]

conn.close()

print("\n==========================================")
print("DATABASE CREATED SUCCESSFULLY!")
print("==========================================")

print("Table name: employees")
print(f"Total rows inserted: {total_rows}")
print(f"\nDatabase location:\n{os.path.abspath(db_path)}")