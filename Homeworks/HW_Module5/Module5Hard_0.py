from time import sleep


class User:
    data = {}

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = int(age)
        User.data[self.nickname] = [self.password, self.age]


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
            User.data[nickname] = [hash(password), age]
            self.current_user = nickname

    def log_out(self):
        self.current_user = None

    def add(self, *video):
        for i in video:
            if i.title in UrTube.videos:
                continue
            else:
                UrTube.videos.append(i.title)

    def get_videos(self, search):
        recommend = []
        for i in UrTube.videos:
            if search.upper() in i.upper():
                recommend.append(i)
        return recommend

    def watch_video(self, title):
        if title in UrTube.videos:
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
v1 = Video('Лучший язык программирования 2024 года', 20)
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
