# import module2 as m2  #  импортируем модуль, даем название

# print('Привет, я из модуля 1')
# print(m2.a)
# m2.say_hi()


# from module2 import a, b, say_hi  # берем переменные и функции из модуля глобально
#
# print('Привет, я из модуля 1')
# print(a+b)
# say_hi()


import module2 as m2  # импортируем модуль, даем название

print('Привет, я из модуля 1')
print(m2.a+m2.b)
m2.say_hi()

