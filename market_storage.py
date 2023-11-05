from random import randint
from products import *
from copy import deepcopy
from current_date import CurrentDate

class Storage:

    def __init__(self):
        self.__capacity = 40  # Общая вместительность склада (в товарных единицах).
        self.__storage = {}  # Здесь хранится информация (объекты) каждой партии товара.
        self.__current_date = CurrentDate()
        self.__products_amount = {}  # Общее количество хранимых единиц товара для каждого класса товаров.
        self.__free_place = self.__capacity  # Свободное место на складе (в товарных единицах).

    # Сохранить товары указанного класса в указанном кол-ве на складе Маркета (если хватает свободного места).
    def save_to_storage(self, product_class: str, products_amount: int) -> bool:

        # Сначала проверяем возможность операции с учётом наличия свободного места на складе.
        if products_amount > self.__free_place:
            print(f"-> Ошибка! Вы пытаетесь разместить {products_amount} ед. товара на кол-ве свободных мест = {self.__free_place}.")
            print("-> Операция прервана, изменения не были сохранены.")
            return False

        else:
            # Если класс товара уже существует в "архивах" Склада.
            if product_class in self.__storage:
                self.__storage[product_class].append(self.__generate_product(product_class, products_amount))
                self.__products_amount[product_class] += products_amount

            # Или же создаём новую ячейку для ранее несуществующего класса товаров.
            else:
                self.__storage[product_class] = []
                self.__storage[product_class].append(self.__generate_product(product_class, products_amount))
                self.__products_amount[product_class] = products_amount

            self.__free_place -= products_amount
            # Сортируем партии товаров одной категории по дате производства в обратном порядке - от самых "свежих" до самых "тухлых".
            # В дальнейшем, при продаже, в первую очередь будут продаваться партии с наиболее давним сроком годности (товары берутся с конца списка).
            self.__storage[product_class].sort(key = lambda x: x.get_manufacture_date(), reverse = True)
            return True

    # Забрать товары указанного класса в указанном кол-ве со склада (если они, конечно, имеются в наличии).
    # Сначала избавляемся от товаров с более давним сроком годности, потом уже - от более свежих (если есть необходимость).
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

                # Освобождаем место на складе после того, как передали товар со склада на продажу.
                self.__free_place += products_amount
                self.__products_amount[product_class] -= products_amount
                return True
        else:
            print("-> Ошибка! Такого товара на складе не существует.")
            return False

    # Вспомогательный метод, автоматически генерирующий случайную дату производства.
    # Дата производства партии зависит от класса товара и его срока годности.
    # Рассчитывается по формуле: Текущая дата - random(3 .. срок_годности_класса_товаров - 10).
    # То есть партия не может быть свежее, чем 3-х дневной давности, но не может быть хуже, чем за 10 дней до окончания срока годности.
    def __random_date(self, value):
        rand_date = deepcopy(self.__current_date)
        rand_date.sub_days(randint(3, value - 10))
        return rand_date.get_date()

    # Вспомогательный метод, который создаёт объект партии товаров нужного класса по названию этого класса.
    def __generate_product(self, product_class: str, products_amount: int) -> Product:

        # При создании продуктов генерируем случайную дату производства, исходя из значения срока годности для класса.
        # У книг и хозяйственных товаров нет срока годности как такового, поэтому просто выбираем достаточно большое число.
        if product_class == "Fruits": return Fruits(products_amount, self.__random_date(30))
        if product_class == "Drinks": return Drinks(products_amount, self.__random_date(180))
        if product_class == "Books": return Books(products_amount, self.__random_date(600))
        if product_class == "Household Goods": return HouseGoods(products_amount, self.__random_date(600))
        if product_class == "Quick Breakfasts": return QuickBreakfasts(products_amount, self.__random_date(360))

    # Метод позволяет обновить "текущую дату" склада исходя из внешней, переданной в качестве аргумента.
    # Сам по себе Склад не умеет прибавлять и вычитать дату, так как это бы дублировало функционал класса Market.
    def date_update(self, new_date: CurrentDate) -> bool:
        self.__current_date = deepcopy(new_date)
        return True

    # Возвращает содержимое склада в сокращённом варианте в виде словаря {product_class: products_amount, ...}.
    def get_storage_info(self):
        return self.__products_amount

    # Возвращает содержимое склада в полном варианте в виде словаря {product_class: [list of Product Objects]}.
    def get_storage_content(self):
        return self.__storage

    # Возвращает текущее количество свободного места на складе (сколько ед. товара ещё можно разместить на складе).
    def get_free_place_info(self):
        return self.__free_place

    # Возвращает кортеж вида (свободное_место, общая_вместимость_склада).
    def get_capacity_info(self):
        return (self.__free_place, self.__capacity)