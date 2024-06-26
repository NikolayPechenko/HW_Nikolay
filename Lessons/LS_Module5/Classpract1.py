class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Класс пользователя, содержащий атрибуты лоигн и пароль
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password_confirm == password and len(str(password)) > 3:
            for i in password:
                if i in '0123456789':
                    self.password = password

if __name__ == '__main__':
    database = Database()
    while True:
        choice = input('Выберите дейтсвие: \n1 Вход \n2 Рестрация \n')
        if choice == '1':
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            if login in database.data:
                if password == database.data[login]:
                    print(f'Велком {login}')
                else:
                    print('Пароль неверный')
        if choice == '2':
            user = User(input('Введите логин: '), password := input('Введите пароль: '), password2 := input('Введите подтверждение пароля: '))
            if password != password2:
                print('Пароли не совпадают, еще раз')
                continue
            database.add_user(user.username, user.password)
        print(database.data)

