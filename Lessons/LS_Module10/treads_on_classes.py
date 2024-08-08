from threading import Thread
import requests


class Getter(Thread):
    res = []
    # URL = 'https://binaryjazz.com/wp-json/genrenator/v1/genre/' -- URL в ините

    def __init__(self, url):
        self.URL = url
        super().__init__()  # необходимо для выполнения логики родительского класса Thread

    def run(self):  # метод, заменяющий target, обязательно run, та самая функция, которая отвечает за выполнение
        response = requests.get(self.URL)
        Getter.res.append(response.json())


threads = []

for i in range(10):
    thread = Getter('https://binaryjazz.com/wp-json/genrenator/v1/genre/')
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(Getter.res)

