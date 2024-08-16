from threading import Thread
from time import sleep
from random import randint
import queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    busy = 0

    def __init__(self, *tables):
        self.q = queue.Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for g in guests:
            a = False
            for i in self.tables:
                if i.guest is None:
                    a = True
                    i.guest = g
                    print(f'{g.name} сел(-а) за стол номер {i.number}')
                    Cafe.busy += 1
                    i.guest.start()
                    break
            if not a:
                self.q.put(g)
                print(f'{g.name} в очереди')

    def discuss_guests(self):
        while not self.q.empty() or Cafe.busy > 0:
            for i in self.tables:
                if i.guest is not None and not i.guest.is_alive():
                    print(f'{i.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {i.number} свободен')
                    i.guest.join()
                    Cafe.busy -= 1
                    i.guest = None
                    if not self.q.empty():
                        i.guest = self.q.get()
                        print(f'{i.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {i.number}')
                        Cafe.busy += 1
                        i.guest.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
