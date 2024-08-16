#  Global interpretor Lock
from threading import Thread


def count_up(name, n):
    for i in range(n):
        print(f'{name} {i + 1} \n', end='')


t1 = Thread(target=count_up, args=('Potok1', 20))
t2 = Thread(target=count_up, args=('Potok2', 50))

t1.start()
t2.start()

t1.join()
t2.join()

