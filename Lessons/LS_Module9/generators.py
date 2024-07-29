import time

start_time = time.time()
my_numbers = [3, 1, 5, 6, 4, 8, 0, 55, 59871]

result = (x * 100 for x in my_numbers)
print(result)  # вычисления не произвелись

for elem in result:  # тут произвелись. Генераторная сборка выполняется только один раз
    print(elem)

# второй пример со временем

result = (x ** 500 for x in my_numbers)
for i in result:
    print(i)

finish_time = time.time()

print(f'Время в мс равно {(finish_time - start_time) * 1000}')


list_1 = [1, 2, 6, 4]
list_2 = [2, 5, 6, 7]

ran = range(10, 30)
zp = zip(list_1, list_2)
mp = filter(str, list_1)

print(list(ran))
print(list(zp))
print(list(mp))


# отсебятина, проверка функции фильтр



list_1 = [1, 2, 6, 4]
mp = filter(lambda x: isinstance(x, str), list_1)
print(list(mp))
