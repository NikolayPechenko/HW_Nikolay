def f1(number):
    return 10 / number


def f2():
    print('Какой хороший день!')  # порядок важен
    result = f1(0)
    return result


try:
    total = f2()
    print(total)
except ZeroDivisionError as exc:
    print(f'Не работает - {exc}')


def f1(number):
    return 10 / number


def f2():
    print('Какой хороший день!')  # порядок важен
    summ = 0
    for i in range(-2, 2):
        summ += f1(i)
        print(summ)
    return summ


try:
    total = f2()  # в Тотал ничего не сохранилось
    print(total)
except ZeroDivisionError as exc:
    print(f'Не работает - {exc}')


def f1(number):
    return 10 / number


def f2():
    print('Какой хороший день!')  # порядок важен
    summ = 0
    for i in range(-2, 2):
        summ += f1(i)
        print(summ)
    return summ


try:
    total = f2()  # в Тотал ничего не сохранилось
    print(total)
except ZeroDivisionError as exc:
    print(f'Не работает - {exc}')


def f1(number):
    return 10 / number


def f2():
    print('Какой хороший день!')  # порядок важен
    summ = 0
    for i in range(-2, 2):
        try:
            summ += f1(i)
            print(summ)
        except ZeroDivisionError as exc:  # перехватили прямо здесь, продолжили работу функции
            print(f'Что-то пошло не так - {exc}')
    return summ


try:
    total = f2()  # в Тотал ничего не сохранилось
    print(total)
except ZeroDivisionError as exc:
    print(f'Не работает - {exc}')
