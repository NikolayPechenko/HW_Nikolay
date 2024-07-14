import os

print('Текущая директория:', os.getcwd())  # путь до директории
if os.path.exists('second'):
    os.chdir('second')  # изменили директорию, в которой находилиcm
else:
    os.mkdir('second')  # создали папку

print('Текущая директория:', os.getcwd())
# print(os.makedirs(r'third\fourth'))  # Позволяет сделать вложенность
print(os.listdir())  # показывает вложенность, но только на один, чтобы все нужен цикл
for i in os.walk('.'):
    print(i)

os.chdir(r'C:\PythonPC\HW-Nikolay\Lessons\LS_Module7')
print('Текущая директория:', os.getcwd())

file = [f for f in os.listdir() if os.path.isfile(f)]  # показывает инфу о файлах
dirs = [d for d in os.listdir() if os.path.isdir(d)]  # показывает инфу о директориях
print(dirs)
print(file)
# os.startfile(file[5])  # открыли файл
print(os.stat(file[5]))
