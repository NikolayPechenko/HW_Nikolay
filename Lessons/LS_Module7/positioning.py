import io
from pprint import pprint


name = 'textx2.txt'
# file = open(name, 'r')
# print(file.tell())
# print(file.read())
# file.close()

# file = open(name, 'a')
# print(file.tell())
# file.seek(13)
# file.write('\n')
# file.write('new')
# print(file.tell())
# file.close()

file = open(name, 'r', encoding='utf-8')  # раскодировали русский язык
print(file.writable())  # показывает, можно ли записывать что-то в файл
print(file.readable())  # показывает, можно ли считать информацию в файле
print(file.seekable())  # показывает, есть ли возможность переместить курсор, зависит от типа файла
# print(file.encoding)  # есть много методов, дающих информацию о файле
print(file.tell())
pprint(file.read())
print(file.tell())  # речь идет не о символах, а о байтах, поэтому результат (65), больше, чем кол-во символов в тексте
file.close()
