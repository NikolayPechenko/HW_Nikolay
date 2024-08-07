from threading import Thread
import requests

# URL = 'https://binaryjazz.com/wp-json/genrenator/v1/genre/'
# res = []
#
# for i in range(20):
#     response = requests.get(URL)  # сделали запрос на сайт
#     page_response = response.json()  # перевели из формата интернета в формат питона
#     res.append(page_response)
#
# print(res)  # Пример не потока, а дефолтного вариата решения задачи, поток ниже

#  Поток


URL = 'https://binaryjazz.com/wp-json/genrenator/v1/genre/'
res = []


def func(url):
    response = requests.get(url)
    page_response = response.json()
    res.append(page_response)


the_first = Thread(target=func, args=(URL, ))  # target - функция, с которой выполнятся поток, args - аргументы функции
the_second = Thread(target=func, args=[URL])  # в args необходимо передавать кортеж(с запятой) или список
the_third = Thread(target=func, args={URL})   # или множество

the_first.start()  # запустили первого человечка (первый поток)
the_second.start()
the_third.start()

the_first.join()  # останавливает работу программы, пока не дождется завершения первого потока
the_second.join()
the_third.join()

print(res)
