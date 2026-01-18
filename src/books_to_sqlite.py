import requests
import sqlite3
import os

# -------------------------------
# Step 1: API Configuration
# -------------------------------
API_URL = "https://openlibrary.org/search.json?q=python"

# -------------------------------
# Step 2: Fetch data from API
# -------------------------------
response = requests.get(API_URL)
response.raise_for_status()  # ensures API call success
data = response.json()

books = data.get("docs", [])[:10]  # limit to 10 records

# -------------------------------
# Step 3: Ensure database folder exists
# -------------------------------
db_path = "databases"
os.makedirs(db_path, exist_ok=True)

db_file = os.path.join(db_path, "books.db")

# -------------------------------
# Step 4: Connect to SQLite
# -------------------------------
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# -------------------------------
# Step 5: Create table
# -------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    publication_year INTEGER
)
""")

# -------------------------------
# Step 6: Insert data
# -------------------------------
for book in books:
    title = book.get("title", "Unknown")
    author = book.get("author_name", ["Unknown"])[0]
    year = book.get("first_publish_year")

    cursor.execute(
        "INSERT INTO books (title, author, publication_year) VALUES (?, ?, ?)",
        (title, author, year)
    )

conn.commit()

# -------------------------------
# Step 7: Display stored data
# -------------------------------
cursor.execute("SELECT * FROM books")
rows = cursor.fetchall()

print("\nStored Books Data:\n")
for row in rows:
    print(row)

# -------------------------------
# Step 8: Close connection
# -------------------------------
conn.close()
