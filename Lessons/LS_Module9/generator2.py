def func_generator(n):
    i = 0
    while i != n:
        yield i
        i += 2


obj = func_generator(10)
for j in obj:
    print(j)


def fibonacci1(n):
    result = []
    a = 0
    b = 1
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result


print(fibonacci1(5))


def fibonacci2(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


obj = fibonacci2(5)
print(obj)
for i in obj:
    print(i)


def fibonacci3():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


obj = fibonacci3()
for i in obj:
    if i > 100:
        break
    else:
        print(i)


