first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(x) - len(y)) for x in first for y in second if (x, y) in list(zip(first, second)) and len(x) != len(y))
print(list(first_result))

second_result = (len(first[i]) == len(second[j]) for i in range(len(first)) for j in range(len(second)) if i == j)
print(list(second_result))
