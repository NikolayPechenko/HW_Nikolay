class Human:  # Родительский (базовый) класс
    head = True

    def __init__(self):
        self.about()


class Student(Human):  # при такой записи класс Student является наследником класса Human
    head = False

    def about(self):
        print('Я студент')


# human = Human()
student = Student()  # при создании экземпляра дочернего класса, также происходит обращение к родительскому,
                     # init для родительского класса сработал для дочернего. SELF сработал как student


# class Human:  # Родительский (базовый) класс
#     head = True
#
#     def say_hello(self):   #  Вынесли метод в родительской класс, доступен для обоих дочерних
#         print('Здравствуйте')
#
#
# class Student(Human):  # при такой записи класс Student является наследником класса Human
#     head = False
#
#     def about(self):
#         print('Я студент')
#
#     def say_hello(self):   #  Вынесли метод в родительской класс, доступен для обоих дочерних
#         print('Привет')
#
#
# class Teacher(Human):
#     pass
#
#
# student = Student()
# teacher = Teacher()
# student.say_hello()
# teacher.say_hello()

