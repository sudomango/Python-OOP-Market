import os
from datetime import datetime
from json_worker import JsonWorker

class Product:
    init_values = JsonWorker().unpack(os.path.dirname(__file__) + "/json/init_values.json")
    products_prices = JsonWorker().unpack(os.path.dirname(__file__) + "/json/purchase_price.json")

    # Большинство начальных значений загружается из файла "/json/init_values.json", который имитирует базу данных.
    def __init__(self, product_class: str, products_amount: int = 1, date: datetime.date = datetime.today().date()):
        self.__id = Product.init_values[product_class]["id"]  # Артикул класса товаров.
        if "expiration" in Product.init_values[product_class]:
            self.__expiration = Product.init_values[product_class]["expiration"]  # Срок годности класса товаров (в днях).
        self.__price_multiply = Product.init_values[product_class]["price_multiply"]  # Наценка на класс товаров.
        self.__amount = products_amount
        self.__manufacture_date = date  # Дата производства товара.
        self.__purchase_price = Product.products_prices[product_class]  # Стоимость закупки класса товаров.
        self.__selling_price = self.__purchase_price * self.__price_multiply  # Стоимость продажи класса товаров.

    def get_manufacture_date(self):
        return self.__manufacture_date

    def get_purchase_price(self):
        return self.__purchase_price

    def get_amount(self):
        return self.__amount

    def set_amount(self, new_amount):
        self.__amount = new_amount
        return True

    def get_selling_price(self):
        return self.__selling_price

    def is_fresh(self, today: datetime.date):
        return (today - self.__manufacture_date).days <= self.__expiration


class Fruits(Product):
    def __init__(self, products_amount, date):
        super().__init__("Fruits", products_amount, date)


class Drinks(Product):
    def __init__(self, products_amount, date):
        super().__init__("Drinks", products_amount, date)


class Books(Product):
    def __init__(self, products_amount, date):
        super().__init__("Books", products_amount, date)


class HouseGoods(Product):
    def __init__(self, products_amount, date):
        super().__init__("Household Goods", products_amount, date)


class QuickBreakfasts(Product):
    def __init__(self, products_amount, date):
        super().__init__("Quick Breakfasts", products_amount, date)