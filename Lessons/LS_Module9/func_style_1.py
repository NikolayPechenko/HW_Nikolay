def get_russian_names():
    return ['Коля', 'Вася', 'Петя']


def get_british_names():
    return ['Ronnie', 'Jack', 'John']


name_getters = [get_russian_names, get_british_names]
for i in name_getters:
    print(i())


def adder(args):
    res = 0
    for j in args:
        res += j
    return res


def multiplier(args):
    res = 1
    for k in args:
        res *= k
    return res


def process_number(numbers, function):
    result = function(numbers)
    print(f'Получилось: {result}')


my_numbers = [3, 1, 5, 6, 4, 8, 0]
process_number(my_numbers, adder)
process_number(my_numbers, multiplier)
process_number(my_numbers, multiplier)


def mul_2(x):
    return x * 2


my_numbers = [3, 1, 5, 6, 4, 8, 0]
result = map(mul_2, my_numbers)  # берет первую функцию и поочередно подставляет из второго аргумента
print(list(result))  # обязательно запаковать


def is_odd(y):
    return y % 2


my_numbers = [3, 1, 5, 6, 4, 8, 0]
result1 = filter(is_odd, my_numbers)  # осталяет значение,если функция - True
a = list(result1)
print(a)

res = map(mul_2, a)
print(list(res))



