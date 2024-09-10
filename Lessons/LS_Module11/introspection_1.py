from typing import Tuple
import inspect

import requests
# help(requests) # - помощь с тем, о чем этот объект (библиотека)

some_number = 2


def some_func(a):
    print(a * a)

# print(some_number.__name__)  # - невозможно узнать имя. Имена имеют функции, классы и тд


print(some_func.__name__)  # можно узнать имя!

print(type(some_number) is int)  # можно узнать тип

print(dir(some_number))  # dir - возвращает список атрибутов и методов, доступных для объекта


class Someclass:
    def __init__(self):
        self.attribute1 = 27

    def method(self, value):
        self.attribute1 = value
        print(self.attribute1)


some_object = Someclass()
attr_name = 'attribute2'

print(hasattr(some_object, attr_name))  # проверяет наличие какого-то атрбиута
print(hasattr(some_object, 'attribute1'))


print(getattr(some_object, 'attribute1'))  # проверяет значение атрибута
print(getattr(some_object, 'attribute2', 'Нет такого!'))
#
for attr_name in dir(requests):
    attr = getattr(requests, attr_name)
    print(attr_name, type(attr))

# сallable проверяет, можем ли мы вызывать этот объект

print(callable(some_number))
print(callable(some_func))

# isinstance проверяет, является ли объект указанным классом

print(isinstance(some_number, int))

# библиотека inspect

print(inspect.ismodule(requests))
print(inspect.isclass(requests))
print(inspect.isfunction(some_func))
print(inspect.isbuiltin(abs))  # является ли объект встроенным в питон

some_func_module = inspect.getmodule(some_func)  # проверяется, в каком модуле находится объект + путь до нее
print(type(some_func_module), some_func_module)