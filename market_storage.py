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

    def save_to_storage(self, product_class: str, products_amount: int) -> bool:
        pass

    def get_from_storage(self, product_class: str, products_amount: int) -> bool:
        pass

    def __increase_capacity(self, n: int):
        if n >= 0:
            self.__capacity += n
            self.__free_place += n
            return True
        else:
            return False

    def get_storage_info(self):
        return self.__products_amount

    def get_storage_content(self):
        return self.__storage

    def get_free_place_info(self):
        return self.__free_place

    def get_capacity_info(self):
        return (self.__free_place, self.__capacity)