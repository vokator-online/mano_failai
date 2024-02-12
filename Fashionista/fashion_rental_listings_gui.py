import sqlite3
import PySimpleGUI as sg
from typing import Any
from populate_db import connection, cursor

def get_listings(
        connection: sqlite3.Connection = connection, 
        cursor: sqlite3.Cursor = cursor
    ):
    with connection:
        cursor.execute("SELECT * FROM listings ORDER BY id")
        listing_list = cursor.fetchall()
    return listing_list

def db_insert_listing(
        values, 
        connection: sqlite3.Connection = connection,
        cursor: sqlite3.Cursor = cursor
    ) -> bool:
    try:
        account_id = int(values["ACCOUNT-ID"])
        listing_name = str(values["-LISTING-NAME-"])
        listing_price = float(values["-LISTING-PRICE-"])
        days_to_rent = int(values["-DAYS-TO-RENT-"])
        likes = 0
    except ValueError:
        sg.PopupOK("Your information appears to be incorrect", title="Error")
        return False
    query = "INSERT INTO listings (account_id, listing_name, listing_price, days_to_rent) VALUES (?, ?, ?, ?)"
    try:
        with connection:
            cursor.execute(query, (account_id, listing_name, listing_price, days_to_rent))
            listing_id = cursor.lastrowid
    except Exception as error:
        sg.PopupOK(f"Database error {error.__class__.__name__}: {error}", title="DB Error")
        return False
    query2 = "INSERT INTO shop (likes, listing_id, account_id) VALUES (?, ?, ?)"
    try:
        with connection:
            cursor.execute(query2, (likes, listing_id, account_id))
    except Exception as error:
        sg.PopupOK(f"Database error {error.__class__.__name__}: {error}", title="DB Error")
        return False
    sg.PopupAutoClose("Insertion Successful", auto_close_duration=2, title="Success")
    return True

def add_listing(listing_manager_window: sg.Window) -> bool:
    listing_manager_window.hide()
    layout = [
        [sg.Text("Account ID", size=10), sg.Input(key="ACCOUNT-ID", size=10, justification="right")],
        [sg.Text("Listing name", size=10), sg.Input(key="-LISTING-NAME-", size=10, justification="right")],
        [sg.Text("Listing price", size=10), sg.Input(key="-LISTING-PRICE-", size=10, justification="right")],
        [sg.Text("Listing days to rent", size=10), sg.Input(key= "-DAYS-TO-RENT-", size= 10, justification= "right")],
        [sg.Button("Add", key="-ADD-"), sg.Button("Cancel", key="-CANCEL-")]
    ]
    window = sg.Window(
        "Add listing | FASHIONISTA PICANTE", 
        layout, 
        element_padding=10,
    )
    success = False
    while True:
        event, values = window.read()
        if event in [sg.WINDOW_CLOSED, "-CANCEL-"]:
            break
        if event == "-ADD-":
            success = db_insert_listing(values)

            if success:
                break
    window.close()
    listing_manager_window.un_hide()
    return success

def db_remove_listing(
        values: tuple[str, Any], 
        listing_list: list[Any],
        connection: sqlite3.Connection = connection,
        cursor: sqlite3.Cursor = cursor
    ) -> bool:
    listing_to_remove = listing_list[values["-LISTINGS-LIST-"][0]]
    if sg.PopupYesNo(f"Remove account ID: {listing_to_remove[1]} listing named: {listing_to_remove[2]}"
                     , title="Remove?") == "Yes":
        try:
            with connection:
                cursor.execute("DELETE FROM listings WHERE id=?", (listing_to_remove[0],))
        except Exception as error:
            sg.PopupOK(f"Database error {error.__class__.__name__}: {error}", title="DB Error")
            return False
        else:
            sg.PopupAutoClose("Removal Successful", auto_close_duration=2, title="Success")
            return True
    else:
        return False
    
def refresh_listing_table(window: sg.Window) -> list[Any]:
    listing_list = get_listings()
    display_listing_list = [(listing[1], listing[2], listing[3], listing[4]) for listing in listing_list]
    window["-LISTINGS-LIST-"].update(values=display_listing_list)
    return listing_list

def manage_listings(main_window: sg.Window):
    main_window.hide()
    listing_list = get_listings()
    display_listing_list = [(listing[1], listing[2], listing[3], listing[4]) for listing in listing_list]
    layout = [
        [sg.Table(display_listing_list, key="-LISTINGS-LIST-",
                     headings=["Account ID","Listing name", "Listing price", "Rental duration"], 
                     expand_x=True, expand_y=True)],
        [
            sg.Button("Add", key="-ADD-"), 
            sg.Button("Remove", key="-REMOVE-"),
            sg.Button("Return", key="-RETURN-"),
        ],
    ]
    window = sg.Window(
        "Listings | FASHIONISTA PICANTE", 
        layout, 
        font="sans-serif 16", 
        element_padding=10,
        size=(1000, 500),
    )
    while True:
        event, values = window.read()
        if event in [sg.WINDOW_CLOSED, "-RETURN-"]:
            break
        if event == "-ADD-":
            if add_listing(window):
                listing_list = refresh_listing_table(window)
        if event == "-REMOVE-":
            if db_remove_listing(values, listing_list):
                listing_list = refresh_listing_table(window)
                
    window.close()
    main_window.un_hide()

