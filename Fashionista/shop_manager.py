import PySimpleGUI as sg
from populate_db import connection, cursor
import random

class ShopManager:
    def __init__(self, cash= 1000, shares= 100, karma= 100):
        self.cash = cash
        self.shares = shares
        self.karma = karma

    def get_shares(self):
        return self.shares

    def get_cash(self):
        return self.cash

    def buy_influencer(self):
        if self.cash > 1000:
            self.cash -= 1000
            with connection:
                influencer_random = random.randint(100, 1000)
                cursor.execute(f"UPDATE shop SET likes = likes + {influencer_random};")
        else:
            sg.PopupError("Not enough cash")

    def buy_youtuber(self):
        if self.cash > 10000:
            # Update shop and deduct cash
            self.cash -= 10000
            with connection:
                youtuber_random = random.randint(1000, 10000)
                cursor.execute(f"UPDATE shop SET likes = likes + {youtuber_random};")
        else:
            sg.PopupError("Not enough cash")
    def buy_superstar(self):
        if self.cash > 100000:
            # Update shop and deduct cash
            self.cash -= 100000
            with connection:
                superstar_random = random.randint(10000, 1000000)
                cursor.execute(f"UPDATE shop SET likes = likes + {superstar_random};")
        else:
            sg.PopupError("Not enough cash")

    def buy_shares(self, qnty: int, stock_price: float):
        if self.cash > stock_price:
            if self.shares + qnty > 100:
                sg.PopupError("There are only 100 shares")
            else:
                self.shares += qnty
                self.cash -= qnty * stock_price
                self.karma += 2
        else:
            sg.PopupError("Not enough $")

    def sell_shares(self, qnty, stock_price: float):
        if self.shares - qnty < 0:
            sg.PopupError("You dont have enough shares")
        else:
            self.shares -= qnty
            self.cash += qnty * stock_price
            self.karma -= 2