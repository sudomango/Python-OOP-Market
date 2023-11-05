from market import Market

def main():

    # Запускаем Супермаркет, проверяем кол-во денег в кассе и текущую дату.
    print("\nЗапускаем новый Супермаркет! Будем специализироваться на Напитках и Книгах.")
    my_market = Market(start_cash = 1200)
    print()
    print("В нашей кассе сейчас:", my_market.check_cashbox())
    print("Текущая дата:", my_market.check_current_date())
    print()
    
    # Узнаём закупочные цены на различные категории товаров.
    my_market.print_purchase_prices()
    print()
    
    # Заказываем 4 товара категории "Напитки" и 2 категории "Книги".
    my_market.make_order("Drinks", 4)
    my_market.make_order("Books", 2)
    print()
    
    # Снова проверяем кол-во денег в кассе после покупок, а также содержимое нашего склада.
    print("В нашей кассе сейчас:", my_market.check_cashbox())
    my_market.print_storage_content()
    # Распечатаем текущее содержимое склада не только в терминале, но ещё и в JSON-файл.
    my_market.print_storage_content("json")
    print()

    # Интересно, сколько времени у нас ушло на закупку товара?
    print("Текущая дата:", my_market.check_current_date())
    print("С запуска Супермаркета прошло дней:", my_market.check_days_from_start())

    # Распечатать стоимость продажи различных категорий товаров в нашем Супермаркете.
    my_market.print_selling_prices()
    print()
    
    # Пробуем продать 10 книг, но так как у нас на складе хранится всего 2, то ничего не выйдет.
    my_market.sell_products("Books", 10)
    print()
    # Хорошо, тогда попробуем продать 2 книги.
    my_market.sell_products("Books", 2)

    # Проверяем кол-во денег в кассе и содержимое склада после продажи.
    print("В нашей кассе сейчас:", my_market.check_cashbox())
    my_market.print_storage_content()
    print()
    print("Текущая дата:", my_market.check_current_date())


main()