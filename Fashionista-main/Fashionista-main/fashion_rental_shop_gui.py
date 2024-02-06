import sqlite3
import PySimpleGUI as sg
import random
from typing import Any
from populate_db import connection, cursor
from shop_manager import ShopManager

def get_shop(
        connection: sqlite3.Connection = connection, 
        cursor: sqlite3.Cursor = cursor
    ):
    with connection:
        cursor.execute("""
SELECT
    accounts.first_name AS account_name,
    accounts.last_name AS last_name,
    shop.account_id,
    accounts.email AS account_email,
    shop.listing_id,
    listings.listing_price AS listing_price,
    listings.listing_name AS listing_name,
    listings.days_to_rent,
    shop.likes,
    CEIL(shop.likes / 25) AS purchases
FROM
    shop
JOIN
    accounts ON shop.account_id = accounts.id
JOIN
    listings ON shop.listing_id = listings.id;
""")
    shop_list = cursor.fetchall()
    with connection:
        random_likes = random.randint(-10, 10)
        cursor.execute(f"UPDATE shop SET likes = likes + {random_likes}")
    return shop_list

def platform_turnover(window: sg.Window):
    shop_list = get_shop()
    total_turnover = 0
    display_shop_list = [(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]) for row in shop_list]
    for row in display_shop_list:
        total_turnover += (row[5]*row[7]*row[9])
    window["-TURNOVER-"].update(f"{total_turnover:.2f}")
    return total_turnover

def stock_price(window: sg.Window, shop_manager: ShopManager):
    price = (platform_turnover(window)*shop_manager.karma/2000)
    return price

def refresh_shop_table(window: sg.Window, shop_manager: ShopManager) -> list[Any]:
    shop_list = get_shop()
    display_shop_list = [(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]) for row in shop_list]
    window["-SHOP-LIST-"].update(values=display_shop_list)
    total_turnover = platform_turnover(window)
    window["STOCK-PRICE"].update(f"{stock_price(window, shop_manager):.2f}")
    window["-CASH-"].update(f"{shop_manager.get_cash():.2f}")
    window["-MANAGER-SHARES-"].update(f"{shop_manager.get_shares()}")
    return shop_list

def manage_upgrades(window: sg.Window, shop_manager: ShopManager):
    window.hide()
    upgrade_layout = [
        [sg.Text("Influencer brings 100 - 1000 likes"), sg.Button("Buy Influencer (1,000$)", key="-BUY-INFLUENCER-")],
        [sg.Text("Youtuber brings 1000 - 10000 likes"), sg.Button("Buy Youruber (10,000$)", key="-BUY-YOUTUBER-")],
        [sg.Text("Superstar brings 10000 - 1000000 likes"), sg.Button("Buy Superstar (100,000$)", key="-BUY-SUPERSTAR-")],
        [sg.Text("Current cash: "), sg.Text(f"{shop_manager.get_cash():.2f}", key="-CASH-")],
        [sg.Button("Return", key="-RETURN-")]
    ]
    upgrade_window = sg.Window(
        "Upgrade | FASHIONISTA PICANTE",
        upgrade_layout,
        font= "sand-serif 14",
        element_padding=5,
        size=(700, 400)
    )
    while True:
        event, values = upgrade_window.read()
        if event in [sg.WINDOW_CLOSED, "-RETURN-"]:
            break        
        if event == "-BUY-INFLUENCER-":
            shop_manager.buy_influencer()
            shop_manager.karma += 1
        if event == "-BUY-YOUTUBER-":
            shop_manager.buy_youtuber()
            shop_manager.karma += 3
        if event == "-BUY-SUPERSTAR-":
            shop_manager.buy_superstar()
            shop_manager.karma += 20
        upgrade_window["-CASH-"].update(f"{shop_manager.get_cash():.2f}")
    upgrade_window.close()
    window.un_hide()

def manage_shop(main_window: sg.Window):
    main_window.hide()
    shop_list = get_shop()
    shop_manager = ShopManager()
    display_shop_list = [(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]) for row in shop_list]
    layout = [
        [sg.Table(display_shop_list, key="-SHOP-LIST-",
                     headings=["Acc name", "Last name", "Acc ID", "Acc email", "Listing ID", "Day price", "Listing name", "Rental period", "Likes", "Purchases"], 
                     expand_x=False, expand_y=False)],
        [sg.Text("Total platform turnover"), sg.Text("refresh", key="-TURNOVER-"), sg.Text("Current FASHIONISTA stock price: "), sg.Text(f"refresh", key="STOCK-PRICE")],
        [sg.Text("Current manager cash"), sg.Text(f"{shop_manager.get_cash()}", key="-CASH-"), sg.Button("Marketing", key="-UPGRADE-")],
        [sg.Text("Current manager shares"), sg.Text(f"{shop_manager.get_shares()}", key="-MANAGER-SHARES-"), sg.Button("Sell 1 share", key="-DUMP-"), sg.Button("Buy 1 share", key="-PUMP-")],
        [sg.Button("Refresh", key="-REFRESH-"),sg.Button("Return", key="-RETURN-")],
    ]
    shop_window = sg.Window(
        "Shop | FASHIONISTA PICANTE", 
        layout, 
        font="sans-serif 12", 
        element_padding=5,
        size=(1300, 400),
        resizable=True
    )
    while True:
        event, values = shop_window.read()
        if event in [sg.WINDOW_CLOSED, "-RETURN-"]:
            break
        if event == "-REFRESH-":
            shop_list = refresh_shop_table(shop_window, shop_manager)
        if event == "-UPGRADE-":
            manage_upgrades(shop_window, shop_manager)
        if event == "-DUMP-":
            shop_manager.sell_shares(1, (platform_turnover(shop_window)/ 20))
            refresh_shop_table(shop_window, shop_manager)
        if event == "-PUMP-":
            shop_manager.buy_shares(1, (platform_turnover(shop_window)/ 20))
            refresh_shop_table(shop_window, shop_manager)
                
    shop_window.close()
    main_window.un_hide()

