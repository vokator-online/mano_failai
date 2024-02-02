-- DROP TABLE bill_line;
INSERT INTO bill_line (bill_id, product_id, quantity) VALUES (?, ?, ?)
''', [(1, 1, 2), (2, 2, 1), (3, 3, 3), (1, 2, 3, 4, 5, 6), (4, 5, 6), (1, 6, 3, 5), (2, 4, 6)])