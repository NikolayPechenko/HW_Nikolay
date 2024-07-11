def custom_write(file_name, strings):
    strings_positions = {}
    j = 1
    for i in strings:
        file = open(file_name, 'a', encoding='utf-8')
        a = file.tell()
        file.write(i + '\n')
        strings_positions[(j, a)] = i
        file.close()
        j += 1
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
