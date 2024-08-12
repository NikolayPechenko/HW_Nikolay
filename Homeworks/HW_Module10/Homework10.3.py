from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:

    def __init__(self):
        self.lock = Lock()
        self.balance = 0

    def deposit(self):
        for i in range(100):
            a = randint(50, 500)
            self.balance += a
            print(f'Пополнение: {a}. Баланс: {self.balance}\n', end='')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for i in range(100):
            b = randint(50, 500)
            print(f'Запрос на {b}\n', end='')
            if b <= self.balance:
                self.balance -= b
                print(f'Снятие: {b}. Баланс: {self.balance}\n', end='')
            else:
                print(f'Запрос отклонён, недостаточно средств\n', end='')
                self.lock.acquire()
            sleep(0.001)


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')



