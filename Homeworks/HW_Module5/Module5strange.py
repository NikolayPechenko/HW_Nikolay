from time import sleep


class User:
    data = {}

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = int(age)
        User.data[nickname] = [password, age]


class Video:
    videos = {}

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = int(duration)
        self.time_now = time_now
        self.adult_mode = adult_mode
        Video.videos[title] = [duration, time_now, adult_mode]


class UrTube:
    users = []
    videos = []
    current_user = None

    def __init__(self):
        pass

    def log_in(self, nickname, password):
        if nickname in User.data:
            if hash(password) == User.data[nickname][0]:
                self.current_user = nickname
            else:
                print('ошибка')

    def register(self, nickname, password, age):
        if nickname in User.data:
            print(f'Пользователь {nickname} уже существует')
        else:
            User.data[nickname] = [password, age]
            self.current_user = nickname

    def log_out(self):
        self.current_user = None


    def add(self, *videos):
        list1 = []
        for v in self.videos:
            list1.append(v.title)
        for video in videos:
            if video.title in list1:
                continue
            else:
                self.videos.append(video)


    def get_videos(self, search):
        search = search.upper()
        recommend = []
        for v in self.videos:
            if search in v.title.upper():
                recommend.append(v.title)
        return recommend

    def watch_video(self, title):
        list2 = []
        for v in self.videos:
            list2.append(v.title)
        if title in list2:
            if self.current_user is None:
                print('Войдите в аккаунт')
            else:
                if (Video.videos[title][2] and User.data[self.current_user][1] >= 18) or Video.videos[title][2] == False:
                    for sex in range(1, Video.videos[title][0] + 1):
                        print(sex, end=' ')
                        sleep(1)
                    print('\nКонец видео')
                else:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 5)
v2 = Video('Для чего девушкам парень программист?', 2, adult_mode=True)


# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
ur.watch_video('Лучший язык программирования 2024 года')