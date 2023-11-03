from market_storage import Storage
from cashbox import Cashbox
from products import *
from json_worker import JsonWorker
from pathlib import Path
from random import randint
from current_date import CurrentDate

class Market:
    def __init__(self, start_cash: float = 200):
        self.__cashbox = Cashbox()  # Инициализируем Кассу.
        self.__cashbox.add_cash(start_cash)
        self.__storage = Storage()  # Инициализируем Склад.
        self.__start_day = CurrentDate().get_date()  # Инициализируем дату запуска Маркета.
        self.__current_day = CurrentDate()  # Инициализируем объект для управления датой.

    def make_order(self, product_class: str, amount: int) -> bool:
        pass

    def sell_products(self, product_class: str, amount: int) -> bool:
        pass

    # Проверить, сколько денег осталось в кассе.
    def check_cashbox(self):
        return self.__cashbox.get_balance()

    # Проверить, сколько места осталось на складе.
    def check_storage(self):
        return self.__storage.get_free_place_info()

    # Метод возвращает кол-во просроченных партий и единиц товара, которые в данный момент хранятся на складе.
    def count_expire_goods(self):
        pass

    # Метод распечатывает кол-во просроченных партий и единиц товара, которые в данный момент хранятся на складе.
    def print_expire_goods(self):
        pass

    # Распечатать содержимое склада (какие товары сейчас на нём хранятся и в каком количестве).
    def print_storage_content(self, destination: str = "terminal") -> bool:
        pass

    # Распечатать текущий прайс-лист на товары (печать также возможна либо в окно терминала, либо в json-файл).
    def print_prices(self, destination: str = "terminal") -> bool:
        pass