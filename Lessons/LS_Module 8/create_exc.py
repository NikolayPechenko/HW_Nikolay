# def greet_person(name):
#     if name == 'ВоланДеМорт':
#         raise Exception('Пошел отсюда чел')
#     print(f'Привет, {name}')
#
#
# greet_person('Ксюша')
# greet_person('ВоланДеМорт')
#
#
# try:
#     raise NameError('Привет, Там')
# except NameError as exc:
#     print(f'Исключение типа {type(exc)} пролетоело мимо, аргументы {exc.args}')
#     raise
#
#
#
# class ProZero(Exception):
#     pass
#
#
# def division(a, b):
#     if b == 0:
#         raise ProZero('Нельзя делить на нуль')
#     return a / b
#
#
# print(division(5, 0))


class Prozero(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info


def division(a, b):
    if b == 0:
        raise Prozero('Нельзя делить на нуль', {'a': a, 'b': b})
    return a / b


try:
    result = division(5, 0)
except Prozero as e:
    print(f'Сообщение {e.message}')
    print(f'Доп инфа {e.extra_info}')