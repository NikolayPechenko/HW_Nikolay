def password(number):
    result = ''
    for i in range(1,number):
        for j in range(i,number):
            if number % (i + j) == 0 and i != j:
                result += str(i)
                result += str(j)
    return result


i = 3
while i > 0:
    n = int(input('Случайное число: '))
    print(password(n))
    i = i - 1


