import sqlite3

connection = sqlite3.connect("platform_db.db")
cursor = connection.cursor()

def create_tables(
        connection: sqlite3.Connection = connection, 
        cursor: sqlite3.Cursor = cursor,
    ):
    queries = [
        '''
CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    email VARCHAR(50)
);
''',
        '''
CREATE TABLE IF NOT EXISTS listings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id INTEGER REFERENCES accounts(id),
    listing_name VARCHAR(50),
    listing_price DECIMAL(18,2),
    days_to_rent INTEGER
);
''',
        '''
CREATE TABLE IF NOT EXISTS shop (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    likes INTEGER,
    listing_id INTEGER REFERENCES listings(id),
    account_id INTEGER REFERENCES accounts(id)
);
''',
    ]
    with connection:
        for query in queries:
            cursor.execute(query)

if __name__ == "__main__":
    create_tables()
