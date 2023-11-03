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
    # Можно распечатать прямо в окно терминала, а можно в json-файл (экспериментально).
    def print_storage_content(self, destination: str = "terminal") -> bool:

        if destination == "terminal":
            products = self.__storage.get_storage_info()
            print()
            if products:
                print("На складе сейчас хранится:\n")
                for prod_key in products.keys():
                    print(f"{prod_key} = {products[prod_key]} ед.")
            else:
                print("На складе сейчас пусто. Совершите закупку товара.")
            return True

        elif destination == "json":
            if not Path("./json_output").exists(): Path("./json_output").mkdir(True, True)
            products = self.__storage.get_storage_info()
            JsonWorker().pack("./json_output/storage_content.json", products)
            print("Файл был успешно записан. Вы можете найти его по адресу ./json_output/storage_content.json")
            return True

        else:
            print("Ошибка! Вы неверно указали объект назначения для печати. Выберите \"terminal\" или \"json\".")
            return False

    # Распечатать текущий прайс-лист на товары (печать также возможна либо в окно терминала, либо в json-файл).
    # Примечание: Распечатываются только те товары, которые есть в наличии на складе (кол-во единиц товара > 0).
    def print_prices(self, destination: str = "terminal") -> bool:

        if destination == "terminal":
            products = self.__storage.get_storage_info()
            print()
            for key in products.keys():
                if products[key] > 0:
                    selling_price = self.__product_class_to_object(key).get_selling_price()
                    print(f"Стоимость продажи для категории товара {key} = {selling_price}")
        elif destination == "json":
            if not Path("./json_output").exists(): Path("./json_output").mkdir(True, True)
            market_prices = {}
            for key in products.keys():
                if products[key] > 0:
                    market_prices[key] = self.__product_class_to_object(key).get_selling_price()
            JsonWorker().pack("./json_output/market_prices.json", market_prices)
            print("Файл был успешно записан. Вы можете найти его по адресу ./json_output/market_prices.json")
            return True
        else:
            print("Ошибка! Вы неверно указали объект назначения для печати. Выберите \"terminal\" или \"json\".")
            return False