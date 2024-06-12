data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

count = 0


def calculate_structure_sum(params):
    global count
    for i in params:
        if isinstance(i, int):
            count += i
        elif isinstance(i, str):
            count += len(i)
        elif isinstance(i, dict):
            i = i.items()
            calculate_structure_sum(i)
        else:
            calculate_structure_sum(i)
    return count


print(calculate_structure_sum(data_structure))


# def calculate_structure_sum(params):
#     global count
#     for i in params:
#         if isinstance(i, int):
#             count += i
#         elif isinstance(i, str):
#             count += len(i)
#             number = ''
#             for j in i:
#                 if j.isdigit():
#                     number += j
#                 elif number != '':
#                     count += int(number) - len(number)
#                     number = ''
#             if number != '':
#                 count += int(number) - len(number)
#         elif isinstance(i, dict):
#             i = i.items()
#             calculate_structure_sum(i)
#         else:
#             calculate_structure_sum(i)
#     return count
#
#
# print(calculate_structure_sum(data_structure))
