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

        if product_class in self.__products_amount:
            available_amount = self.__products_amount[product_class]
            if products_amount > available_amount:
                print(f"-> Ошибка! Вы пытаетесь взять {products_amount} ед. товара из доступного кол-ва = {available_amount} ед.")
                print("-> Операция прервана, изменения не были сохранены.")
                return False
            else:
                products_amount_copy = products_amount
                # Удаление продуктов со склада согласно их количеству.
                while products_amount_copy != 0:
                    last_product = self.__storage[product_class][-1]
                    last_product_amount = last_product.get_amount()
                    if products_amount_copy < last_product_amount:
                        self.__storage[product_class][-1].set_amount(last_product_amount - products_amount_copy)
                        products_amount_copy = 0
                    else:
                        self.__storage[product_class].pop()
                        products_amount_copy -= last_product_amount

                self.__free_place += products_amount
                self.__products_amount[product_class] -= products_amount
                return True
        else:
            print("-> Ошибка! Такого товара на складе не существует.")
            return False

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