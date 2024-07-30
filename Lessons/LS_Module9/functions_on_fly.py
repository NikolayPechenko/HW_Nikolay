from pprint import pprint

my_func = lambda x: x + 10

print(my_func(10))
print(type(my_func))

my_numbers = [3, 1, 5, 6]
your_numbers = [5, 2, 7, 9]

print(list(map(lambda x: x + 10, my_numbers)))

result = map(lambda x, y: x + y, my_numbers, your_numbers)  # - складываются попарно
print(list(result))


def get_multiplier_v1(n):
    if n == 2:
        def multiplier(x):
            return x * 2

    elif n == 3:
        def multiplier(x):
            return x * 3

    else:
        raise Exception('Я могу умножать только на 2 и на 3')

    return multiplier  # вернули функцию, чтобы использовать ее в map


by2 = get_multiplier_v1(2)
by3 = get_multiplier_v1(3)

result = map(by2, my_numbers)
print(list(result))
result = map(by3, my_numbers)
print(list(result))


def get_multiplier_v2(n):
    def multiplier(x):
        return x * n  # n будет в области видимости, так как будет взят из функции высшего порядке, вызванной ранее

    return multiplier


by_5 = get_multiplier_v2(5)
print(by_5(x=40))

by_10 = get_multiplier_v2(10)
print(list(map(by_10, my_numbers)))


def matrix(some_list):
    def multiply_column(x):
        res = []
        for i in some_list:
            res.append(i * x)
        return res

    return multiply_column


matrix_on_my_numbers = matrix(my_numbers)
result = map(matrix_on_my_numbers, your_numbers)
pprint(list(result))


class Multiplier:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n * x


by_100500 = Multiplier(n=100500)  # создали объект класса (это будет функция, благодаря методу call)
result = by_100500(x=42)
print(result)

result = map(by_100500, my_numbers)
print(list(result))


