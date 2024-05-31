# def summa(n):
#     if n == 0:
#         return 0
#     else:
#         return n + summa(n - 1)
#
#
# print(summa(5))


stack = []
stack.append(1)
print('Добавили элемент: ', stack)
stack.append(2)
print('Добавили элемент: ', stack)
stack.append(3)
print('Добавили элемент: ', stack)
print('Полный список: ', stack)
stack.pop()
print('Убрали элемент: ', stack)
stack.pop()
print('Убрали элемент: ', stack)
stack.pop()
print('Убрали элемент: ', stack)



# def get_multiplied_digits(number):
#     number = int(str(number).replace('0', '1'))
#     if number // 10 == 0:
#         return number
#     else:
#         return number % 10 * (get_multiplied_digits(number // 10))
#
#
# n = int(input())
# print(get_multiplied_digits(n))
