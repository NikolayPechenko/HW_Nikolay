my_dict = {'Николай': 1999, 'Никита': 1998, 'Вланетин': 1986, 'Ксения': 1999}
print(my_dict)
print(my_dict['Николай'])
print(my_dict.get('Антон', 'без ошибки'))
my_dict['Евгений'] = 1995
my_dict.update({'Петр': 1971})
print(my_dict)
a = my_dict.pop('Евгений')
print(a)
print(my_dict)

my_set = {3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 'Nikolay', 'Nikolay', True, True}
print(my_set)
my_set.add('Nikita')
my_set.add(1897)
print(my_set)
my_set.remove(6)
print(my_set)
