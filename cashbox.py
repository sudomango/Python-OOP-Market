class Cashbox:

    def __init__(self, model: str = "Model MK-03"):
        self.__model = model
        self.__balance = 0

    def add_cash(self, amount: float) -> bool:
        if amount >= 0:
            self.__balance += amount
            return True
        else:
            print("-> Ошибка! Вы ввели неверную сумму.")
            return False

    def sub_cash(self, amount: float) -> bool:
        if amount >= 0 and self.__balance >= amount:
            self.__balance -= amount
            return True
        else:
            print("-> Ошибка! Вы ввели неверную сумму или в кассе недостаточно средств.")
            return False

    def get_balance(self):
        return self.__balance