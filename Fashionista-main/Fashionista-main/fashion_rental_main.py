import PySimpleGUI as sg
from fashion_rental_account_gui import manage_accounts
from fashion_rental_listings_gui import manage_listings
from fashion_rental_shop_gui import manage_shop

sg.theme("dark")
sg.set_options(font="sans-serif 18")

main_layout = [
    [sg.Button("Accounts", key="-ACCOUNTS-", size=10),sg.Button("SHOP", key="-SHOP-", size=10)],
    [sg.Button("Listings", key="-LISTINGS-", size=21)]
]

main_window = sg.Window(
    "FASHIONISTA PICANTE", 
    main_layout, 
    element_justification="center", 
    element_padding=20,
    resizable=True
)

while True:
    event, values = main_window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-ACCOUNTS-':
        manage_accounts(main_window)
    if event == '-SHOP-':
        manage_shop(main_window)
    if event == '-LISTINGS-':
        manage_listings(main_window)



