-- DROP TABLE bill;
INSERT INTO bill (purchase_datetime, cashier_id, customer_id) VALUES (?, ?, ?)
''', [('2024-01-30 10:00:00', 1, 1), ('2024-01-30 11:30:00', 2, 2), ('2024-01-30 12:45:00', 1, 3)])