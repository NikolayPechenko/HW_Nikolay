from threading import Thread
from time import sleep
import queue


def producer(queue123):
    c = 0
    while True:
        message = 'ping ' + str(c)
        queue123.put(message)
        c += 1




def worker(queue123):
    while True:
        message = queue123.get()
        print(message)
        sleep(1)


q = queue.Queue()
t1 = Thread(target=producer, args=(q,))
t2 = Thread(target=worker, args=(q,))

t1.start()
t2.start()

t1.join()
t2.join()

