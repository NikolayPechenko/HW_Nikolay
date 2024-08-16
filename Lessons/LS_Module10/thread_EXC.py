import threading
from threading import Thread, excepthook
from time import sleep


def some_func():  # простой вариант
    sleep(1)
    raise Exception


# def thread_func():
#     try:
#         some_func()
#     except Exception as e:
#         print('Wow!!!')
#
#
# t1 = Thread(target=thread_func)
# t2 = Thread(target=thread_func)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()

def excepthook(args):  # вызвали и переопределили excepthook, настраиваем по своему усмотрению
    print(args.thread.name)


threading.excepthook = excepthook

t1 = Thread(target=some_func)
t2 = Thread(target=some_func)

t1.start()
t2.start()

t1.join()
t2.join()
