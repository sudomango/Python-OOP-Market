from datetime import datetime, timedelta

class CurrentDate:

    def __init__(self):
        self.__date = datetime.today().date()

    def add_days(self, number_of_days: int) -> bool:
        if number_of_days >=0 and number_of_days <= 3000:
            self.__date += timedelta(days = number_of_days)
            return True
        else:
            print("Ошибка! Количество дней указано неверно. Укажите целое число в диапазоне 0 .. 3000.")
            return False

    def sub_days(self, number_of_days: int) -> bool:
        if number_of_days >=0 and number_of_days <= 3000:
            self.__date -= timedelta(days = number_of_days)
            return True
        else:
            print("Ошибка! Количество дней указано неверно. Укажите целое число в диапазоне 0 .. 3000.")
            return False

    def get_date(self):
        return self.__date

    def print_date(self):
        print(self.__date.strftime("%d.%m.%Y"))