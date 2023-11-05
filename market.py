import market_interface

from market_storage import Storage
from cashbox import Cashbox
from products import *
from json_worker import JsonWorker
from pathlib import Path
from random import randint
from current_date import CurrentDate

class Market(market_interface.Market_ABC):
    def __init__(self, start_cash: float = 200):
        self.__cashbox = Cashbox()  # Инициализируем Кассу.
        self.__cashbox.add_cash(start_cash)  # Добавляем в кассу стартовый капитал.
        self.__storage = Storage()  # Инициализируем Склад.
        self.__start_day = CurrentDate()  # Инициализируем дату запуска Маркета.
        self.__current_day = CurrentDate()  # Инициализируем объект для управления текущей датой.

    # Заказать n единиц товара определённой категории у поставщика (при условии, что есть нужное кол-во денег и свободного места на складе).
    def make_order(self, product_class: str, amount: int) -> bool:
        price = self.__product_class_to_object(product_class).get_purchase_price() * amount
        if self.__cashbox.get_balance() >= price and self.__storage.get_free_place_info() >= amount:
            self.__cashbox.sub_cash(price)
            self.__send_date_to_storage()
            self.__storage.save_to_storage(product_class, amount)
            self.__current_day.add_days(2)  # Прибавляем 2 дня за покупку (и доставку) партии товара.

            print(f"-> Закупка прошла успешно! Вы потратили {price} денег из кассы и купили {amount} ед. товара {product_class}.")
            return True
        else:
            if self.__cashbox.get_balance() < price: print("-> Ошибка! В кассе недостаточно денег для закупки товара.")
            if self.__storage.get_free_place_info() < amount: print("-> Ошибка! На складе недостаточно места для хранения товара.")
            print("-> Операция прервана, изменения не были сохранены.")
            return False

    # Продать n единиц товара определённой категории со склада (при условии, что нужное количество товара имеется на складе).
    def sell_products(self, product_class: str, amount: int) -> bool:
        self.__send_date_to_storage()
        if self.__storage.get_from_storage(product_class, amount):
            if self.count_expire_goods()[1] == 0:
                selling_procents = randint(60, 90) / 100  # Если все товары - свежие, процент продаж будет 60-90%.
            else:
                selling_procents = randint(30, 50) / 100  # Если на складе есть несвежие товары, процент продаж будет 30-50%.
            cash = self.__product_class_to_object(product_class).get_selling_price() * int(amount * selling_procents)

            print(f"-> Продажа прошла успешно! Вы продали {int(amount * selling_procents)} ед. товара за {amount} дней и получили {cash} денег в кассу.")

            self.__cashbox.add_cash(cash)
            self.__current_day.add_days(amount * 1)  # Прибавляем по 1 дню за каждую продаваемую единицу товара.
            return True
        else:
            print("-> Ошибка! Продажа прервана, изменения не были сохранены.")
            return False

    # Вспомогательный метод, который создаёт временный объект товара по названию класса.
    def __product_class_to_object(self, product_class: str) -> Product:
        if product_class == "Fruits": return Fruits()
        if product_class == "Drinks": return Drinks()
        if product_class == "Books": return Books()
        if product_class == "Household Goods": return HouseGoods()
        if product_class == "Quick Breakfasts": return QuickBreakfasts()

    # Вспомогательный метод, позволяющий передать значение "текущей даты" другому объекту.
    # Так как мы вручную меняем значение текущей даты в объекте данного класса, её также вручную надо обновлять у объектов других классов (при необходимости).
    def __send_date_to_storage(self) -> bool:
        self.__storage.date_update(self.__current_day)
        return True

    # Проверить, сколько денег осталось в кассе.
    def check_cashbox(self) -> float:
        return self.__cashbox.get_balance()

    # Проверить, сколько места осталось на складе.
    def check_storage_free_place(self) -> int:
        return self.__storage.get_free_place_info()

    # Проверить, какая сегодня дата (в программе).
    def check_current_date(self) -> str:
        return self.__current_day.get_date_string()

    # Проверить, сколько дней прошло от запуска нашего магазина.
    def check_days_from_start(self) -> int:
        delta = self.__current_day.get_date() - self.__start_day.get_date()
        return delta.days

    # Метод возвращает кол-во просроченных партий и единиц товара, которые в данный момент хранятся на складе (в виде кортежа).
    def count_expire_goods(self) -> tuple:
        number_of_expire_batches = 0
        number_of_expire_units = 0
        storage = self.__storage.get_storage_content()
        for key in storage.keys():
            products_list = storage[key]
            # Переворачиваем список, так как на складе он был отсортирован, начиная от самых свежих товаров.
            products_list.reverse()
            for product in products_list:
                if not product.is_fresh(self.__current_day.get_date()):
                    number_of_expire_batches += 1
                    number_of_expire_units += product.get_amount()
                else:
                    break  # Если мы встретили свежую партию, то все дальнейшие партии в категории будут ещё свежее (благодаря сортировке).
        return (number_of_expire_batches, number_of_expire_units)

    # Метод распечатывает кол-во просроченных партий и единиц товара, которые в данный момент хранятся на складе.
    def print_expire_goods(self) -> bool:
        count_of_expire_goods = self.count_expire_goods()
        if count_of_expire_goods == (0, 0):
            print("Все товары на складе свежие. Так держать!")
        else:
            print(f"На данный момент на складе {count_of_expire_goods[0]} просроченных партий, в которых {count_of_expire_goods[1]} ед. просроченного товара.")
        return True

    # Распечатать JSON-файл с закупочными ценами в окне терминала.
    def print_purchase_prices(self) -> bool:
        prices = JsonWorker().unpack(os.path.dirname(__file__) + "/json/purchase_price.json")
        for key in prices.keys():
            print(f"Стоимость закупки 1 ед. для категории товара {key} = {prices[key]}")
        return True

    # Распечатать текущее содержимое склада (какие товары сейчас на нём хранятся и в каком количестве).
    # Можно распечатать в окне терминала, а можно в JSON-файл (экспериментально).
    def print_storage_content(self, destination: str = "terminal") -> bool:

        if destination == "terminal":
            products = self.__storage.get_storage_info()
            print()
            if products:
                print("На складе сейчас хранится:")
                for prod_key in products.keys():
                    print(f"Категория {prod_key} = {products[prod_key]} ед.")
            else:
                print("На складе сейчас пусто. Совершите закупку товара.")
            return True

        elif destination == "json":
            if not Path("./json_output").exists(): Path("./json_output").mkdir(True, True)
            products = self.__storage.get_storage_info()
            JsonWorker().pack("./json_output/storage_content.json", products)
            print("-> Файл был успешно записан. Вы можете найти его по адресу ./json_output/storage_content.json")
            return True

        else:
            print("-> Ошибка! Вы неверно указали объект назначения для печати. Выберите \"terminal\" или \"json\".")
            return False

    # Распечатать текущий прайс-лист на категории товаров (печать также возможна либо в окне терминала, либо в JSON-файл).
    def print_selling_prices(self, destination: str = "terminal") -> bool:

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
            print("-> Файл был успешно записан. Вы можете найти его по адресу ./json_output/market_prices.json")
            return True

        else:
            print("-> Ошибка! Вы неверно указали объект назначения для печати. Выберите \"terminal\" или \"json\".")
            return False