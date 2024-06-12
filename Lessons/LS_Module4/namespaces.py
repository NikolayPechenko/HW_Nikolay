import math


# def square(x):  # область видимости этой функции стала ОБЪЕМЛЮЩЕЙ для функции снизу
#     d = x ** 2
#     def even(x):
#         if d % 2 == 0:
#             print('Четное')
#         else:
#             print('Нечетное')
#     even(x)
#     return d
#
#
# a = 5
# b = square(3)
# print(a)
# print(b)


def square(x):
    d = x ** 2
    def even(x):
        nonlocal d  # переопределяем d для функции сверху
        d = x / 2
        if d % 2 == 0:
            print('Четное')
        else:
            print('Нечетное')
    even(x)
    return d


a = 5
b = square(6)
print(a)
print(b)
