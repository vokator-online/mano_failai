import sqlite3

connection = sqlite3.connect("platform_db.db")
cursor = connection.cursor()

def populate_accounts(
        connection: sqlite3.Connection = connection, 
        cursor: sqlite3.Cursor = cursor,
    ):
    accounts = [
        ('Aldona', 'Giraite', 'aldaona@giraite.lt'),
        ('Benas', 'Babausis', 'benas@babausis.lt'),
        ('Aleksas', 'Gurksnis', 'ale@gurksnis.lt')
    ]
    query = "INSERT INTO accounts (first_name, last_name, email) VALUES (?, ?, ?)"
    with connection:
        cursor.executemany(query, accounts)

def populate_listings(
        connection: sqlite3.Connection = connection, 
        cursor: sqlite3.Cursor = cursor,
    ):
    listings = [
        (1, 'Dior bag', 5.00, 1),
        (2, 'Gucci skirt', 14.20, 10),
        (3, 'Armani belt', 13.37, 3),
    ]
    query = "INSERT INTO listings (account_id, listing_name, listing_price, days_to_rent) VALUES (?, ?, ?, ?)"
    with connection:
        cursor.executemany(query, listings)

def populate_shop(
        connection: sqlite3.Connection = connection, 
        cursor: sqlite3.Cursor = cursor,
    ):
    shop_listings = [
        (420, 1, 1),
        (13, 2, 2),
        (102, 3, 3)
    ]
    query = "INSERT INTO shop (likes, listing_id, account_id) VALUES (?, ?, ?)"
    with connection:
        cursor.executemany(query, shop_listings)

if __name__ == "__main__":
    populate_accounts()
    populate_listings()
    populate_shop()
