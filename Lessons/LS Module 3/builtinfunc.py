# salary = [2300, 2648.15, 1250, 6951.59, 3374]
# print(round(sum(salary) / len(salary), 2), 'средняя зп')
# print(round(max(salary), 2), 'максимальная зп')
# print(min(salary), 'минимальная зп')
#
# names = ['Denis', 'Nikolay', 'Alisa', 'Ksyusha', 'Nikolay']
#
# zipped = dict(zip(names, salary))
# print(zipped['Denis'], 'зп Дениса')
#
#
# a = [2, False]
# b = 'h'
# print(any(b))  # хотя бы один элмент True
# print(all(b))  # Все элементы True
# print(dir(b))  # Что можно сделать
# print(isinstance(a, str))  # проверяет, относится ли объект к какому-то типу
# c = [1, 1, 1]
# d = [1, 1, 1]
# print(c == d)
# print(id(c))  # id объекта
# print(id(d))  # id объекта
# print(help(a))  # помощь в работе с объектом какого-либо типа
#
#
# def pomoshnik():
#     """
#     Это функция для ассиста
#     """
#     pass
#
#
# print(help(pomoshnik))  # вызов функции помощника, где функция документирования первая
# print(pomoshnik.__doc__)


# def count_sum_and_lengths(data):
#     total_sum = 0
#     total_length = 0
#
#     for item in data:
#         if isinstance(item, (int, float)):
#             total_sum += item
#         elif isinstance(item, str):
#             total_length += len(item)
#         elif isinstance(item, (list, tuple, set)):
#             sub_sum, sub_length = count_sum_and_lengths(item)
#             total_sum += sub_sum
#             total_length += sub_length
#         elif isinstance(item, dict):
#             sub_sum, sub_length = count_sum_and_lengths(item.items())
#             total_sum += sub_sum
#             total_length += sub_length
#
#     return total_sum, total_length
#
#
# data_structure = [
#     [1, 2, 3],
#     {'a': 4, 'b': 5},
#     (6, {'cube': 7, 'drum': 8}),
#     "Hello",
#     ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
#
# result_sum, result_length = count_sum_and_lengths(data_structure)
# print("Сумма всех чисел:", result_sum)
# print("Сумма длин всех строк:", result_length)


def count_sum_and_lengths(data):
    total_sum = 0
    total_length = 0

    for item in data:
        if isinstance(item, (int, float)):
            total_sum += item
        elif isinstance(item, str):
            total_length += len(item)
            number = ""
            for char in item:
                if char.isdigit():
                    number += char
                elif number:
                    total_sum += int(number)
                    total_length -= len(number)
                    number = ""
            if number:
                total_sum += int(number) - len(number)
        elif isinstance(item, list) or isinstance(item, tuple):
            sub_sum, sub_length = count_sum_and_lengths(item)
            total_sum += sub_sum
            total_length += sub_length
        elif isinstance(item, dict):
            sub_sum, sub_length = count_sum_and_lengths(item.values())
            total_sum += sub_sum
            total_length += sum(len(str(key)) for key in item.keys()) + sub_length
        elif isinstance(item, set):
            sub_sum, sub_length = count_sum_and_lengths(list(item))
            total_sum += sub_sum
            total_length += sub_length

    return total_sum, total_length

data_structure = [
    'Ur2ban2'
]

result_sum, result_length = count_sum_and_lengths(data_structure)
print("Сумма всех чисел:", result_sum)
print("Сумма длин всех строк:", result_length)



