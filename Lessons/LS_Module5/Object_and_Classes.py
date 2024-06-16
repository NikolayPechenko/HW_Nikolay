class Toyota:

    def __init__(self):
        self.color = 'Бардовый фантомас'
        self.price = '100000 миллионов'
        self.max_velocity = '258 км/ч'
        self.current_velocity = '0 км/ч'
        self.engine_rpm = 0

    def start(self):
        print('Завелась с толкача')
        self.engine_rpm = 900

    def go(self):
        print('Тронулись ебать')
        self.engine_rpm = 2000
        self.current_velocity = '20 км/ч'


my_car = Toyota()
print('Цвет:', my_car.color)
print('Цена:', my_car.price)
print('Максимальная скорость: ', my_car.max_velocity)
print('Обороты:', my_car.engine_rpm)

my_car.start()
print('Обороты:', my_car.engine_rpm)
my_car.go()
print('Обороты:', my_car.engine_rpm)
print('Скорость:', my_car.current_velocity)


class Human:
    def __init__(self, name, age):  # метод init, конструктор класса, то, что будет создаваться при инициализации объекта
        self.name = name  # определяем атрибуты, характеристику (name), атрибуты - переменные внутри класса
        self.age = age
        self.say_info()

    def say_info(self):
        print(f'Меня зовут {self.name}, мне {self.age} лет')

    def birthday(self):
        self.age = self.age + 1
        print(f'У меня День Рождения, мне теперь {self.age} лет')


den = Human('Дениска', 25)  # создан объект класса Human, объект уникальный
maxim = Human('Макс',56)
print(den.name, den.age)
print(maxim.name, maxim.age)
den.surname = 'Попов'  # можем самомтоятельно добавлять атрибуты и менять их
print(den.surname)

den.birthday()



