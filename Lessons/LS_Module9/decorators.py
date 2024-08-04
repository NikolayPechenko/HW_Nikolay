import sys
import time

def null_decorator(func):  # декоратор должен возвращать функцию
    return func


def greet():
    return 'Hello'


greet = null_decorator(greet)  # декоратор = обертка, дополняющая функционал

print(greet())


@null_decorator  # сразу декорирует функцию
def greet():
    return 'Hello kids'


print(greet())
print(greet(), 123)


def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper  # теперь greet это функция wrapper в обновленнам функционалом


@uppercase
def greet():
    return 'Hello guys'


print(greet())


def time_track(func):
    def surrogate(*args, **kwargs):  # в данном случае kwargs не требуется
        started_at = time.time()

        result = func(*args, **kwargs)  # в данном случае kwargs не требуется

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд')
        return result
    return surrogate


@time_track
def digits(*args):
    total = 1
    for i in args:
        total *= i ** 5000
    return len(str(total))


sys.set_int_max_str_digits(100000)

result = digits(5659, 6559, 5917, 5588)
print(result)

