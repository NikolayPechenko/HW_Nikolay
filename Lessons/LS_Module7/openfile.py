from pprint import pprint


name = 'textx.txt'
file = open(name, 'r')  # r, w, a  r - чтение, w - write, a - append
pprint(file.read())
file.close()  # закрыли файл, если меняли что-то внутри, файлы сохранятся.

name2 = 'textx2.txt'
file1 = open(name2, 'w')  # файл в режиме записи
file1.write('Hello')  # написали в файл

file1 = open(name2, 'a')  # файл в режиме добавления
file1.write(' World')  # добавили текст

file1 = open(name2, 'r')
pprint(file1.read())

print(file1.tell())  # нашли курсор
print(file1.seek(5))  # передвинули курсор
pprint(file1.read())  # файл читается с нового места

# file1 = open(name2, 'r+')  # файл в режим чтения + записи, тогда можно написать с другого места
# print(file1.seek(6))  # передвинули курсор
# file1.write('z')

# file1 = open(name2, 'r')
# print(file1.read())
# file1.seek(0)
# a = len(file1.read())
# print(a)


file1.close()




