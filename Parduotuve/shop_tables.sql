-- DROP TABLE product;
CREATE TABLE IF NOT EXISTS product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50),
    price INTEGER
    );

-- DROP TABLE customer;
CREATE TABLE IF NOT EXISTS customer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
    );

-- DROP TABLE bill;
CREATE TABLE IF NOT EXISTS bill (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    purchase_datetime TIME,
    cashier_id INTEGER,
    customer_id INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customer (id)
);

-- DROP TABLE bill_line;
CREATE TABLE IF NOT EXISTS bill_line (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bill_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (bill_id) REFERENCES bill (id),
    FOREIGN KEY (product_id) REFERENCES product (id)
);
