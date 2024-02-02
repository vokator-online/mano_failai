import sqlite3
import PySimpleGUI as sg

# -- DB modelis: parduotuvė:
# -- * product (id, name, price)
# -- * customer (id, first_name, last_name)
# -- * bill (id, purchase_datetime, cashier_id, customer_id)
# -- * bill_line (id, bill_id, product_id, quantity)
# -- Užklausos:
# -- * daugiausiai parduodami produktai
# -- * didžiausia produkto apyvarta
# -- * geriausias klientas
# -- * didžiausia saskaita

tables = (  """CREATE TABLE IF NOT EXISTS product (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(50),
                price DECIMAL(10,2)
            )""",
            """CREATE TABLE IF NOT EXISTS customer (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name VARCHAR(50),
                last_name VARCHAR(50)
            )""",
            """CREATE TABLE IF NOT EXISTS bill (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                purchase_datetime DATETIME,
                cashier_id INTEGER,
                customer_id INTEGER REFERENCES customer(id)
            )""",
            """CREATE TABLE IF NOT EXISTS bill_line (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                quantity INTEGER,
                bill_id INTEGER REFERENCES bill(id),
                product_id INTEGER REFERENCES product(id)
            )"""
)

def create_table(tables, connector, cursor):
    for table in tables:
        cursor.execute(table)
        connector.commit()

def main_window():
    sg.theme()
    layout = [
        [sg.Text("Client First Name : ", size=15), sg.Input(size=20, key="-FIRST_NAME-"),
         sg.Text("Product Name : ", size=15, pad=((40,0), (0,0))), sg.Input(size=20, key="-PRODUCT_NAME-")],
        [sg.Text("Client Last Name : ", size=15), sg.Input(size=20, key="-LAST_NAME-"),
         sg.Text("Product Price: ", size=15, pad=((40,0), (0,0))), sg.Input(size=20, key="-PRODUCT_PRICE-")],
        [sg.Button("List of all clients", size=15, key="-LIST_CLIENTS-"),
         sg.Button("Add new Client", size=15, key="-NEW_CLIENT-"),
         sg.Button("List of all Products", size=15, key="-LIST_PRODUCTS-", pad=((80,0), (0,0))),
         sg.Button("Add new Product", size=15, key="-NEW_PRODUCT-")],
        [sg.Button("Drop all Clients", size=15, key="-DROP_CLIENT-"),
         sg.Button("Drop all Products", size=15, key="-DROP_PRODUCTS-", pad=((233,0), (0,0)))],

        [sg.Text(pad=((0,0), (40,0)))],

        [sg.Text("Purchase Time : ", size=15), sg.Input(size=20, key="-PURCHASE_TIME-"),
         sg.Text("Product Quantity: ", size=15, pad=((40,0), (0,0))), sg.Input(size=20, key="-PRODUCT_QUANTITY-")],
        [sg.Text("  Cashier ID : ", size=15), sg.Input(size=20, key="-CASHIER_ID-"),
         sg.Text("     Bill ID : ", size=15, pad=((40,0), (0,0))), sg.Input(size=20, key="-BILL_ID-")],
        [sg.Text("    Client ID : ", size=15), sg.Input(size=20, key="-CLIENT_ID-"),
         sg.Text("   Product ID: ", size=15, pad=((40,0), (0,0))), sg.Input(size=20, key="-PRODUCT_ID-")],         
        [sg.Button("List of all Bills", size=15, key="-LIST_BILLS-"),
         sg.Button("Add new Bill", size=15, key="-NEW_BILL-"),
         sg.Button("Roster of Bill Lists", size=15, key="-LIST_BILL_LISTS-", pad=((80,0), (0,0))),
         sg.Button("Add Bill List", size=15, key="-NEW_BILL_LIST-")],
        [sg.Button("Drop all Bills", size=15, key="-DROP_BILLS-"),
         sg.Button("Drop all Bill Lists", size=15, key="-DROP_BILL_LISTS-", pad=((233,0), (0,0)))],
        
        [sg.Button("Exit", size=18, pad=((250, 0), (45, 0)))]
    ]
    window = sg.Window("Parduotuve", layout)
    return window

def add_data_to_db_2(winput_1, winput_2):
    data_1 = winput_1.get()
    winput_1.update("")
    data_2 = winput_2.get()
    winput_2.update("")
    return data_1, data_2

def add_data_to_db_3(winput_1, winput_2, winput_3):
    data_1 = winput_1.get()
    winput_1.update("")
    data_2 = winput_2.get()
    winput_2.update("")
    data_3 = winput_3.get()
    winput_3.update("")
    return data_1, data_2, data_3

def show_list(list_of_date, column1, column2, column3=""):
    layout = [
        [sg.Table(values=[list(list_of_date[i]) for i in range(len(list_of_date))], justification="center",
                  headings=["ID", column1, column2, column3], num_rows=min(25, len(list_of_date)))],
        [sg.Button("Close", size=15, pad=((80, 0), (20, 0)))]
    ]

    window = sg.Window("Table", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Close":
            window.close()
            break

if __name__ == "__main__":
    connector = sqlite3.connect("parduotuve.db")
    cursor = connector.cursor()
    create_table(tables, connector, cursor)
    window = main_window()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == "-NEW_CLIENT-":
            first_name, last_name = add_data_to_db_2(window["-FIRST_NAME-"], window["-LAST_NAME-"])
            with connector:
                cursor.execute("INSERT INTO customer (first_name, last_name) VALUES(?, ?)",
                               (first_name, last_name))
        elif event == "-NEW_PRODUCT-":
            name, price = add_data_to_db_2(window["-PRODUCT_NAME-"], window["-PRODUCT_PRICE-"])
            with connector:
                cursor.execute("INSERT INTO product (name, price) VALUES(?, ?)",
                               (name, price))            
        elif event == "-NEW_BILL-":
            purchase_datetime, cashier_id, customer_id = add_data_to_db_3(window["-PURCHASE_TIME-"],
                                                            window["-CASHIER_ID-"], window["-CLIENT_ID-"])
            with connector:
                cursor.execute("INSERT INTO bill (purchase_datetime, cashier_id, customer_id) VALUES(?, ?, ?)",
                               (purchase_datetime, cashier_id, customer_id))
        elif event == "-NEW_BILL_LIST-":
            quantity, bill_id, product_id = add_data_to_db_3(window["-PRODUCT_QUANTITY-"], window["-BILL_ID-"],
                                                             window["-PRODUCT_ID-"])
            with connector:
                cursor.execute("INSERT INTO bill_line (quantity, bill_id, product_id) VALUES(?, ?, ?)",
                               (quantity, bill_id, product_id))
        elif event == "-DROP_CLIENT-":
            with connector:
                cursor.execute("DROP TABLE customer")
                cursor.execute(tables[1])
        elif event == "-DROP_PRODUCT-":
            with connector:
                cursor.execute("DROP TABLE product")
                cursor.execute(tables[0])
        elif event == "-DROP_BILLS-":
            with connector:
                cursor.execute("DROP TABLE bill")
                cursor.execute(tables[2])
        elif event == "-DROP_BILL_LISTS-":
            with connector:
                cursor.execute("DROP TABLE bill_line")
                cursor.execute(tables[3])
        elif event == "-LIST_CLIENTS-":
            with connector:
                cursor.execute("SELECT * FROM customer")
                list_of_date = cursor.fetchall()
                show_list(list_of_date, "First Name", "Last Name")            
        elif event == "-LIST_PRODUCTS-":
            with connector:
                cursor.execute("SELECT * FROM product")
                list_of_date = cursor.fetchall()
                show_list(list_of_date, "Name", "Price")  
        elif event == "-LIST_BILLS-":
            with connector:
                cursor.execute("SELECT * FROM bill")
                list_of_date = cursor.fetchall()
                show_list(list_of_date, "Purchase datetime", "Cashier ID", "Customer ID")  
        elif event == "-LIST_BILL_LISTS-":
            with connector:
                cursor.execute("SELECT * FROM bill_line")
                list_of_date = cursor.fetchall()
                show_list(list_of_date, "Quantity", "Bill ID", "Product ID") 

    window.close()
    connector.close()
