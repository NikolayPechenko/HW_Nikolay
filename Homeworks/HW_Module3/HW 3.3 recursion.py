def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) != 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        if first == 0:
            return 1
        else:
            return first


print(get_multiplied_digits(2060))


mp = 1
n = 55
while n > 0:
    mp = mp * (n % 10)
    n = n // 10
print(mp)

result = 0
numbers = 56
for digit in str(numbers):  # Преобразуем число в строку и берем абсолютное значение
    result += int(digit)
print(result)