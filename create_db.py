

import sqlite3

conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    product TEXT,
    amount INTEGER
)
""")

cursor.execute("DELETE FROM sales")

cursor.executemany("INSERT INTO sales VALUES (?, ?)", [
    ("Shoes", 2000),
    ("Bags", 1500),
    ("Watches", 3000),
    ("Phones", 4000),
    ("Laptops", 5000)
])

conn.commit()
conn.close()