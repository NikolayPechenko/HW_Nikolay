# import requests
# from threading import Thread, Event
# import queue
#
# ACCESS_TOKEN = 'CXyFeSBw2lAdG41xkuU3LS6a_nwyxwwCz2dCkUohw-rw0C49x2HqP__6_4is5RPx'
# RANDOM_GENRE_API_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'
# GENIUS_API_URL = 'https://api.genius.com/search'
# GENIUS_URL ='https://genius.com'
#
# all_songs = []
#
#
# class Genre(Thread):
#     def __init__(self, queue, stop_event):  # можно использовать обычный counter, но это не топ-вариант
#         self.queue = queue
#         self.stop_event = stop_event
#         super().__init__()
#
#     def run(self):
#         while not self.stop_event.is_set():
#             genre = requests.get(RANDOM_GENRE_API_URL).json()
#             self.queue.put(genre)
#
#
# class Genius(Thread):
#     def __init__(self, queue):
#         self.queue = queue
#         super().__init__()
#
#     def run(self):
#         genre = self.queue.get()
#         print(self.queue.qsize())
#         data = requests.get(GENIUS_API_URL, params={'access_token': ACCESS_TOKEN, 'q': genre})
#         data = data.json()
#         try:
#             song_id = data['response']['hits'][0]['result']['api_path']
#             all_songs.append(f'genre: {genre}, song: {GENIUS_URL}{song_id}/apple_music_player')
#         except IndexError as e:
#             self.run()  # в случае неудачи снова вызвает метод run
#
#
# queue = queue.Queue()
# stop_event = Event()
#
# genre_list = []
# genius_list = []
#
# for _ in range(5):
#     t = Genre(queue, stop_event)
#     t.start()
#     genre_list.append(t)
#
# for _ in range(100):
#     t = Genius(queue)
#     t.start()
#     genius_list.append(t)
#
# for t in genius_list:
#     t.join()
# stop_event.set()  # перевели в значение True, именно здесь потому что поток Genre бесконечен
#
# for t in genre_list:
#     t.join()
#
# print(queue.qsize())
# print(all_songs)
# print(len(all_songs))

import requests
from threading import Thread, Event
import queue

ACCESS_TOKEN = 'CXyFeSBw2lAdG41xkuU3LS6a_nwyxwwCz2dCkUohw-rw0C49x2HqP__6_4is5RPx'
RANDOM_GENRE_API_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'
GENIUS_API_URL = 'https://api.genius.com/search'
GENIUS_URL ='https://genius.com'


class Genre(Thread):
    def __init__(self, queue, stop_event):  # можно использовать обычный counter, но это не топ-вариант
        self.queue = queue
        self.stop_event = stop_event
        super().__init__()

    def run(self):
        while not self.stop_event.is_set():
            genre = requests.get(RANDOM_GENRE_API_URL).json()
            self.queue.put(genre)


class Genius(Thread):
    all_songs = []

    def __init__(self, queue, stop_event, counter):
        self.queue = queue
        self.stop_event = stop_event
        self.counter = counter
        super().__init__()

    def run(self):
        while not self.stop_event.is_set():
            genre = self.queue.get()
            print(self.queue.qsize())
            data = requests.get(GENIUS_API_URL, params={'access_token': ACCESS_TOKEN, 'q': genre})
            data = data.json()
            print(data)
            try:
                song_id = data['response']['hits'][0]['result']['api_path']
                self.all_songs.append(f'genre: {genre}, song: {GENIUS_URL}{song_id}/apple_music_player')
                if self._list_is_filled():
                    self.stop_event.set()
            except IndexError as e:
                self.run()  # в случае неудачи снова вызвает метод run

    def _list_is_filled(self):
        return len(self.all_songs) > self.counter


queue = queue.Queue()
stop_event = Event()
counter = 10
genre_list = []
genius_list = []

for _ in range(6):
    t = Genre(queue, stop_event)
    t.start()
    genre_list.append(t)

for _ in range(10):
    t = Genius(queue, stop_event, counter)
    t.start()
    genius_list.append(t)

for t in genius_list:
    t.join()

# stop_event.set()  # перевели в значение True, именно здесь потому что поток Genre бесконечен


print(queue.qsize())
print(Genius.all_songs)
print(len(Genius.all_songs))
a = (Genius.all_songs[0:10])
print(a)
print(len(a))




