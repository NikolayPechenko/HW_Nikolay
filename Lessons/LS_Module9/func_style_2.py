# list_comp_1=[x*2 for x in collection]
# list_comp_2=[x*2 for x in collection if x > 5] - фильтрация элементов в списке
# list_comp_3=[x*2 if x > 2 else x * 10 for x in collection] - не фильтрация элементов в списке, а проверка условий для выполнения разных операций
# list_comp_4=[x*y for x in collection_1 for y in collection_2] - генерация для двух элементов
def is_odd(x):
    return x % 2


def by_3(x):
    return x * 3


my_numbers = [3, 1, 5, 6, 4, 8, 0]

result = map(by_3, filter(is_odd, my_numbers))
print(list(result))

list2 = [by_3(x) for x in my_numbers if x % 2]  # - списковая сборка
print(list2)

list3 = [x * 2 if x > 2 else x * 10 for x in my_numbers]
print(list3)

my_numbers1 = [1, 4]
your_numbers = [5, 2, 7, 9]

result = [x * y for x in my_numbers1 for y in your_numbers]
print(result)

result = [x * y for x in my_numbers1 for y in your_numbers if x % 2]
print(result)

result = [x * y for x in my_numbers1 for y in your_numbers if x % 2 and y // 3]
print(result)

result = {x: x ** 2 for x in your_numbers}
print(result)