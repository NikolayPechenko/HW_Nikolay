# def test_func(*params):
#     print('Тип: ', type(params))
#     print('Аргумент: ', params)
#
#
# test_func(1,2,3,4)


# def summator(txt, *values, type1='summator'):
#     s = 0
#     for i in values:
#         s += i
#     return f'{txt}{s} {type1}'
#
# print(summator('Сумма указанных значений: ',1,2,3,4, type1='summa'))


# def info(*types, **values):
#     print('Тип:', type(values))
#     print('Аргумент:', values)
#     for key, value in values.items():
#         print(key, value)
#     print(types)
#
#
# info(1, 2, 34, name='Denis', course='Python')


def my_sum(n, *args, txt = 'Сумма чисел:'):
    s = 0
    for i in range(len(args)):
        s += args[i] ** n
    print(txt, s)


my_sum(3,4,5,6, txt='Сумма кубов:')
