import os
from datetime import datetime
from json_worker import JsonWorker

# Объект класса "Товар" представляет собой партию товара определённого класса. В каждой партии может быть 1 или более товаров указанного класса.

class Product:
    init_values = JsonWorker().unpack(os.path.dirname(__file__) + "/json/init_values.json")
    products_prices = JsonWorker().unpack(os.path.dirname(__file__) + "/json/purchase_price.json")

    # Большинство начальных значений загружается из файла "/json/init_values.json", который используется вместо базы данных.
    def __init__(self, product_class: str, products_amount: int = 1, date: datetime.date = datetime.today().date()):
        self.__manufacture_date = date  # Дата производства текущей партии товара.
        if "expiration" in Product.init_values[product_class]:  # Атрибут expiration создаётся не для всех дочерних классов.
            self.__expiration = Product.init_values[product_class]["expiration"]  # Срок годности класса товаров (в днях).
        self.__amount = products_amount  # Количество единиц товара в текущей партии.
        self.__price_multiply = Product.init_values[product_class]["price_multiply"]  # Наценка-множитель на класс товара.
        self.__purchase_price = Product.products_prices[product_class]  # Стоимость закупки класса товаров.
        self.__selling_price = self.__purchase_price * self.__price_multiply  # Стоимость продажи класса товаров в нашем Маркете.

    def get_manufacture_date(self) -> datetime.date:
        return self.__manufacture_date

    def get_purchase_price(self) -> float:
        return self.__purchase_price

    def get_amount(self) -> int:
        return self.__amount

    def set_amount(self, new_amount: int) -> bool:
        self.__amount = new_amount
        return True

    def get_selling_price(self) -> float:
        return self.__selling_price

    # Метод возвращает True, если срок годности данной партии товара в норме, если партия просрочена - возвращает False.
    def is_fresh(self, today: datetime.date) -> bool:
        return (today - self.__manufacture_date).days <= self.__expiration


# 5 дочерних классов от класса Product: Fruits, Drinks, Books, HouseGoods (хоз. товары), QuickBreakfasts (быстрые завтраки).
# У классов Books и HouseGoods нет срока годности, товары этого класса не могут быть просроченными.

class Fruits(Product):
    def __init__(self, products_amount: int = 1, date: datetime.date = datetime.today().date()):
        super().__init__("Fruits", products_amount, date)


class Drinks(Product):
    def __init__(self, products_amount: int = 1, date: datetime.date = datetime.today().date()):
        super().__init__("Drinks", products_amount, date)


class Books(Product):
    def __init__(self, products_amount: int = 1, date: datetime.date = datetime.today().date()):
        super().__init__("Books", products_amount, date)

    # У книжной продукции нет срока годности (по крайней мере, в данной программе).
    def is_fresh(self, today: datetime = datetime.now()) -> bool:
        return True


class HouseGoods(Product):
    def __init__(self, products_amount: int = 1, date: datetime.date = datetime.today().date()):
        super().__init__("Household Goods", products_amount, date)

    # У хозяйственных товаров нет срока годности (по крайней мере, в данной программе).
    def is_fresh(self, today: datetime = datetime.now()) -> bool:
        return True


class QuickBreakfasts(Product):
    def __init__(self, products_amount: int = 1, date: datetime.date = datetime.today().date()):
        super().__init__("Quick Breakfasts", products_amount, date)