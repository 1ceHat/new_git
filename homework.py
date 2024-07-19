from threading import Thread, Lock
import time


class BankAccount:
    __lock = Lock()

    def __init__(self, amount: int = 20_000_000):
        self.__amount = amount

    def deposit(self, amount):
        with BankAccount.__lock:
            self.__amount += amount
            print(f'Зачислено: {amount}. Баланс: {self.__amount}')

    def withdraw(self, amount):
        with BankAccount.__lock:
            if self.__amount - amount < 0:
                print(f'Недостаточно средств! Не хватает: {amount - self.__amount}')
            else:
                self.__amount -= amount
                print(f'Списано: {amount}. Баланс: {self.__amount}')


def deposit_task(account, amount):
    for _ in range(100):
        account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(100):
        account.withdraw(amount)


account = BankAccount()
deposit_thread = Thread(target=deposit_task, args=(account, 100_000))
withdraw_thread = Thread(target=withdraw_task, args=(account, 200_000))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
