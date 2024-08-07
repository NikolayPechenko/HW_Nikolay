import sys
import time


def func_gen_dec(precision):
    def dec(func):
        def wrapper(*args, **kwargs):
            started_at = time.time()

            result = func(*args, **kwargs)

            ended_at = time.time()
            elapsed = round(ended_at - started_at, precision)  # сами выбираем, какое округление требуется
            print(f'Функция работала {elapsed} секунд')
            return result
        return wrapper
    return dec


@func_gen_dec(6)
def digits(*args):
    total = 1
    for i in args:
        total *= i ** 5000
    return len(str(total))


sys.set_int_max_str_digits(100000)

# time_track_precision = func_gen_dec(10)
# digits = time_track_precision(digits)
result = digits(1,2,3,4,5,6)
print(result)

