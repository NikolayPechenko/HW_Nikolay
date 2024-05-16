num1 = 5
num2 = 3
sum = num1 + num2
print(sum)
result = sum + num1 * num2
print(result)


name = 'Вишня'
price = int(input('Введите цену товара '))
mass = int(input('Введите вес товара (в кг) '))
money = int(input('Введите количество денег у пользователя '))
change = money - mass * price
sum = mass * price
print(name)
print(mass, 'кг')
print(price, 'руб/кг')
print('Итого: ', sum, 'руб')
print('Сдача: ', change, 'руб')


N = int(input('Введите любое натуральное число '))
print('Купи конструктор\n' * N)


favourite = input('Какое ваще любимое дело? ')
N = int(input('Введите сколько раз вы хотите записать о том, что обожаете свое любимое дело '))
print (('Обожаю ' + favourite + '\n') * N)



