import csv
import sqlite3
import os

# -------------------------------
# Step 1: File paths
# -------------------------------
csv_file_path = "data/user.csv"
db_folder = "databases"
db_file_path = os.path.join(db_folder, "users.db")

# -------------------------------
# Step 2: Ensure database folder exists
# -------------------------------
os.makedirs(db_folder, exist_ok=True)

# -------------------------------
# Step 3: Connect to SQLite database
# -------------------------------
conn = sqlite3.connect(db_file_path)
cursor = conn.cursor()

# -------------------------------
# Step 4: Create users table
# -------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

# -------------------------------
# Step 5: Read CSV and insert data
# -------------------------------
with open(csv_file_path, mode="r", newline="", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (row["name"], row["email"])
        )

# Commit changes
conn.commit()

# -------------------------------
# Step 6: Display inserted records
# -------------------------------
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print("\nInserted User Records:\n")
for row in rows:
    print(row)

# -------------------------------
# Step 7: Close connection
# -------------------------------
conn.close()
