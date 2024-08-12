# race_condition - состояние гонки

from threading import Thread, Lock

lock = Lock()
x = 0


def thread_task():
    global x
    for i in range(10_000_000):
        #   x = x + 1  # операция не атомарно (> 1 действия). Для корректной работы нужна блокировка
        lock.acquire()  # закрыли замок
        x = x + 1
        lock.release()  # открыли замок
        # with lock:  -  возможная реализация блокировки
        #     x = x + 1


def thread_task():
    global x
    for i in range(1_000_000):
        try:
            lock.acquire()
            x = x + 1
        finally:
            lock.release()


def main():
    global x
    x = 0
    t1 = Thread(target=thread_task)
    t2 = Thread(target=thread_task)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


for j in range(10):
    main()
    print(x)
