from abc import ABC, abstractmethod

class Market_ABC(ABC):

    # Конструктор класса Market. Создание объекта = Market(), либо Market(стартовое_количество_денег).
    @abstractmethod
    def __init__(self, start_cash: float = 200):
        pass

    # Заказать n единиц товара определённой категории у поставщика (при условии, что есть нужное кол-во денег и свободного места на складе).
    @abstractmethod
    def make_order(self, product_class: str, amount: int) -> bool:
        pass

    # Продать n единиц товара определённой категории со склада (при условии, что нужное количество товара имеется на складе).
    @abstractmethod
    def sell_products(self, product_class: str, amount: int) -> bool:
        pass

    # Проверить, сколько денег осталось в кассе.
    @abstractmethod
    def check_cashbox(self) -> float:
        pass

    # Проверить, сколько места осталось на складе.
    @abstractmethod
    def check_storage(self) -> int:
        pass

    # Проверить, какая сегодня дата (в программе).
    @abstractmethod
    def check_current_date(self) -> str:
        pass

    # Проверить, сколько дней прошло от запуска нашего магазина.
    @abstractmethod
    def check_days_from_start(self) -> int:
        pass

    # Метод возвращает кол-во просроченных партий и единиц товара, которые в данный момент хранятся на складе (в виде кортежа).
    @abstractmethod
    def count_expire_goods(self) -> tuple:
        pass

    # Метод распечатывает кол-во просроченных партий и единиц товара, которые в данный момент хранятся на складе.
    @abstractmethod
    def print_expire_goods(self) -> bool:
        pass

    # Распечатать JSON-файл с закупочными ценами в окне терминала.
    @abstractmethod
    def print_purchase_prices(self) -> bool:
        pass

    # Распечатать текущее содержимое склада (какие товары сейчас на нём хранятся и в каком количестве).
    # Можно распечатать в окне терминала, а можно в JSON-файл (экспериментально). Пример вызова: market.print_storage_content("json").
    @abstractmethod
    def print_storage_content(self, destination: str = "terminal") -> bool:
        pass

    # Распечатать текущий прайс-лист на категории товаров (печать также возможна либо в окне терминала, либо в JSON-файл).
    @abstractmethod
    def print_selling_prices(self, destination: str = "terminal") -> bool:
        pass