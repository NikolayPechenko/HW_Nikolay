#def print_params(a, b, c): #*args (упаковка позиционных параментров - один элемент), **kwargs (упаковка именованных параментров - словарей)


# def print_params(*numbers):
#         print(*numbers)
# print_params(1,2,3)


# def print_params(a, b, c):
#     print(a, b, c)
#
#
# list_ = [1, 2, 3]
# # print_params(list_) ошибка, нужно 3 параметра
# print_params(*list_)


def print_params(a, b, c):
    print(a, b, c)


dict_ = {'a': 1, 'b': 2, 'c': 3} # имена параметров соответствуют именам ключей
print_params(**dict_)

def print_params(**kwargs):
    print(kwargs)


dict_ = {'a': 1, 'b': 2, 'c': 3} # имена параметров соответствуют именам ключей
print_params(**dict_)

def print_params(**kwargs):
    for i, j in kwargs.items():
        print(i, j)


dict_ = {'a': 1, 'b': 2, 'c': 3} # имена параметров соответствуют именам ключей
print_params(**dict_)


def print_params(a, b, c):
    print(a, b, c)

list = [1, 2]
dict_ = {'c': 3}
print_params(*list, **dict_)


