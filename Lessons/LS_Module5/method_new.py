# class User:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):  #  метод new переопределяет базовый метод object,
#                                         # singleton применяется, чтобы объект класса создавался единожды
#         print('Я в нью')
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#
#     def __init__(self):
#         print('Я в ините')
#
#
# user1 = User()
# user2 = User()  #  объекты ведут к одному адресу в памяти, это все один объект
# user1.name = 'KIA'
# print(user1.name)
# print(user2.name)


class User:
    __instance = None

    def __new__(cls, *args, **kwargs):  #  метод new переопределяет базовый метод object,
                                        # singleton применяется, чтобы объект класса создавался единожды
        print('Я в нью')
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, *args, **kwargs):  # распаковка
        print('Я в ините')
        self.args = args
        self.kwargs = kwargs  #  при такой записи ниже данная строчка необязательна
        self.name = kwargs.get('name')
        for key, values in kwargs.items():
            setattr(self, key, values)


other = [1, 2, 3]
user = {'name': 'Nick', 'age': 25, 'gender': 'male'}

user = User(*other, **user)
print(user.args)
print(user.kwargs)
print(user.name)
print(user.age)
print(user.gender)
