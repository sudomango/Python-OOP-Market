from random import randint
from products import *
from current_date import CurrentDate

class Storage:

    def __init__(self):
        self.__capacity = 40
        self.__storage = {}
        self.__current_date = CurrentDate()
        self.__products_amount = {}
        self.__free_place = self.__capacity

    # Сохранить товары указанного класса в указанном кол-ве на складе Маркета (если хватает свободного места).
    def save_to_storage(self, product_class: str, products_amount: int) -> bool:
        pass

    # Забрать товары указанного класса в указанном кол-ве со склада (если они, конечно, имеются в наличии).
    def get_from_storage(self, product_class: str, products_amount: int) -> bool:
        pass

    # Вспомогательный метод, позволяющий увеличить вместительность склада.
    def __increase_capacity(self, n: int):
        if n >= 0:
            self.__capacity += n
            self.__free_place += n
            return True
        else:
            return False

    # Возвращает содержимое склада в виде словаря {product_class: products_amount, ...}.
    def get_storage_info(self):
        return self.__products_amount

    # Возвращает содержимое склада в виде словаря {product_class: [list of Product Objects]}.
    def get_storage_content(self):
        return self.__storage

    # Возвращает количество свободного места на складе (в момент вызова метода).
    def get_free_place_info(self):
        return self.__free_place

    # Возвращает кортеж вида (свободное_место, общая_вместимость_склада).
    def get_capacity_info(self):
        return (self.__free_place, self.__capacity)