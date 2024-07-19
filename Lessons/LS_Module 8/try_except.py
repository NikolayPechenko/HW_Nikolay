# try:
#     пишем код с возможной ошибкой
# except:
#     пишем блок в случае возникновения ошибки

try:
    i = 0
    print(10/i)
except:
    print('неправильно')


try:
    i = '*'
    print(10/i)
    print(10/0)  # выведется только первый except
except ZeroDivisionError:  # указали ошибку
    print('неправильно')
except NameError:
    print('дурак')
except TypeError:
    print('бестолочь')
except ValueError:
    print('дегенерат')
except SyntaxError:
    print('бездарь')


try:
    truba = a + b
    truba = 10 / 0
except (ZeroDivisionError, NameError):  # перечислили имена классов ошибок
    print('Устояли')


try:
    a = 10 / 0
except ZeroDivisionError as exc:  # дали название классу ошибки
    print(f'Устояли, возник {exc}')


try:
    file = open('blabla.txt', 'r')
except OSError as exc:
    print(f'Что-то пошло, возник {exc.args}')  # вызвали параметры ошибки


# блок else выполняется, если нет ошибки, блок finally выполняется в любом случае. Блоки необязательные

i = int(input('Введите число: '))

try:
    result = 10 * (1/i)
except ZeroDivisionError as exc:
    print(f'Неуадача, {exc}')
else:
    print('Хорошо', result)
finally:
    print('Поработать и домашка')


