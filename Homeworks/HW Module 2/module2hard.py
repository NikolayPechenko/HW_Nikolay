def password(number):
    result = ''
    for i in range(1,number):
        for j in range(i,number):
            if number % (i + j) == 0 and i != j:
                result += str(i)
                result += str(j)
    return result


n = int(input('Случайное число: '))
print(password(n))


