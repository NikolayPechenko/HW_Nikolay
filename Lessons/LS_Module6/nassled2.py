class Human:  # Родительский (базовый) класс
    head = True
    _legs = True  # одно нижнее подчеркивания делает использование только локальным, важно для импорта
    __arms = True  # два нижн.подчеркивания, не будет изменено в дочерних классах

    def say_hello(self):   # Вынесли метод в родительской класс, доступен для обоих дочерних
        print('Здравствуйте')


class Student(Human):  # при такой записи класс Student является наследником класса Human
    arms = False
    def about(self):
        print('Я студент')


class Teacher(Human):
    pass


human = Human()
student = Student()
print(student._Human__arms)
print(student.arms)
print(human._Human__arms)
print(student._legs)