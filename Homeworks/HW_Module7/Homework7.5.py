import os
import time

print('Текущая директория:', os.getcwd())
directory = '.'

for root, dirs, files in os.walk(directory):
    for file in files:
        path = os.path.join(root, file)
        filetime = os.path.getmtime(path)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        size = os.path.getsize(path)
        parent_dir = os.path.dirname(path)
        print(f'Обнаружен файл: {file}, Путь: {path}, Размер: {size} байт, '
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
