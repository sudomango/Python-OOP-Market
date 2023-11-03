import os
from datetime import datetime
from json_worker import JsonWorker

class Product:
    init_values = JsonWorker().unpack(os.path.dirname(__file__) + "/json/init_values.json")
    products_prices = JsonWorker().unpack(os.path.dirname(__file__) + "/json/purchase_price.json")

    def __init__(self, product_class, products_amount, date):
        pass

    def get_manufacture_date(self):
        pass

    def get_purchase_price(self):
        pass

    def get_amount(self):
        pass

    def set_amount(self, new_amount):
        pass

    def get_selling_price(self):
        pass

    def is_fresh(self, today):
        pass


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