import sqlite3

conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

# create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    sales INTEGER
)
""")

# insert sample data
cursor.execute("INSERT INTO products (name, category, sales) VALUES ('Laptop', 'Electronics', 150)")
cursor.execute("INSERT INTO products (name, category, sales) VALUES ('Phone', 'Electronics', 200)")
cursor.execute("INSERT INTO products (name, category, sales) VALUES ('Shoes', 'Fashion', 120)")
cursor.execute("INSERT INTO products (name, category, sales) VALUES ('Watch', 'Fashion', 90)")
cursor.execute("INSERT INTO products (name, category, sales) VALUES ('Headphones', 'Electronics', 180)")

conn.commit()
conn.close()

print("Sample data inserted successfully")