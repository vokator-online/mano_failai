import sqlite3
import PySimpleGUI as sg
from typing import Any
from populate_db import connection, cursor

def get_accounts(
        connection: sqlite3.Connection = connection, 
        cursor: sqlite3.Cursor = cursor
    ):
    with connection:
        cursor.execute("SELECT * FROM accounts ORDER BY id")
        account_list = cursor.fetchall()
    return account_list

def db_insert_account(
        values, 
        connection: sqlite3.Connection = connection,
        cursor: sqlite3.Cursor = cursor
    ) -> bool:
    try:
        first_name = str(values["-FIRST-NAME-"])
        last_name = str(values["-LAST-NAME-"])
        email = str(values["EMAIL"])
    except ValueError:
        sg.PopupOK("Your information appears to be a number", title="Error")
        return False
    query = "INSERT INTO accounts (first_name, last_name, email) VALUES (?, ?, ?)"
    try:
        with connection:
            cursor.execute(query, (first_name, last_name, email))
    except Exception as error:
        sg.PopupOK(f"Database error {error.__class__.__name__}: {error}", title="DB Error")
        return False
    sg.PopupAutoClose("Insertion Successful", auto_close_duration=2, title="Success")
    return True

def add_account(account_manager_window: sg.Window) -> bool:
    account_manager_window.hide()
    layout = [
        [sg.Text("First name", size=10), sg.Input(key="-FIRST-NAME-", size=10, justification="right")],
        [sg.Text("Last  name:", size=10), sg.Input(key="-LAST-NAME-", size=10, justification="right")],
        [sg.Text("Email", size=10), sg.Input(key= "EMAIL", size=10, justification= "right")],
        [sg.Button("Add", key="-ADD-"), sg.Button("Cancel", key="-CANCEL-")]
    ]
    window = sg.Window(
        "Add account | FASHIONISTA PICANTE", 
        layout, 
        element_padding=10,
    )
    success = False
    while True:
        event, values = window.read()
        if event in [sg.WINDOW_CLOSED, "-CANCEL-"]:
            break
        if event == "-ADD-":
            success = db_insert_account(values)
            if success:
                break
    window.close()
    account_manager_window.un_hide()
    return success

def db_remove_account(
        values: tuple[str, Any], 
        account_list: list[Any],
        connection: sqlite3.Connection = connection,
        cursor: sqlite3.Cursor = cursor
    ) -> bool:
    account_to_remove = account_list[values["-ACCOUNT-LIST-"][0]]
    if sg.PopupYesNo(f"Remove account: {account_to_remove[1]} {account_to_remove[2]}"
                     f"Email: {account_to_remove[3]} ", title="Remove?") == "Yes":
        try:
            with connection:
                cursor.execute("DELETE FROM accounts WHERE id=?", (account_to_remove[0],))
        except Exception as error:
            sg.PopupOK(f"Database error {error.__class__.__name__}: {error}", title="DB Error")
            return False
        else:
            sg.PopupAutoClose("Removal Successful", auto_close_duration=2, title="Success")
            return True
    else:
        return False

def refresh_account_table(window: sg.Window) -> list[Any]:
    account_list = get_accounts()
    display_account_list = [(account[1], account[2], account[3]) for account in account_list]
    window["-ACCOUNT-LIST-"].update(values=display_account_list)
    return account_list

def manage_accounts(main_window: sg.Window):
    main_window.hide()
    account_list = get_accounts()
    display_account_list = [(account[1], account[2], account[3]) for account in account_list]
    layout = [
        [sg.Table(display_account_list, key="-ACCOUNT-LIST-",
                     headings=["First Name", "Last Name", "Email"], 
                     expand_x=True, expand_y=True)],
        [
            sg.Button("Add", key="-ADD-"), 
            sg.Button("Remove", key="-REMOVE-"),
            sg.Button("Return", key="-RETURN-"),
        ],
    ]
    window = sg.Window(
        "Accounts | FASHIONISTA PICANTE", 
        layout, 
        font="sans-serif 16", 
        element_padding=10,
        size=(1000, 500),
        resizable=True
    )
    while True:
        event, values = window.read()
        if event in [sg.WINDOW_CLOSED, "-RETURN-"]:
            break
        if event == "-ADD-":
            if add_account(window):
                account_list = refresh_account_table(window)
        if event == "-REMOVE-":
            if db_remove_account(values, account_list):
                account_list = refresh_account_table(window)

    window.close()
    main_window.un_hide()