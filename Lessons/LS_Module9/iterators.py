import sys
from itertools import repeat
ex_iterator = repeat('4', 100000)
print(ex_iterator)
print(f'Размер интератора - {sys.getsizeof(ex_iterator)}')

list1 = '4' * 100000
print(f'Размер списка - {sys.getsizeof(list1)}')


class Iter:

    def __init__(self):
        self.first = 'Первый элемент'
        self.second = 'Второй элемент'
        self.third = 'Третий элемент'
        self.i = 0

    def __iter__(self):
        self.i = 0  # обнулили счетчик
        return self  # возвращаем ссылку на себя, чтобы объект класса стал итератором

    def __next__(self):  # метод возвращает значение по требованию python, ленивое вычислениt
        self.i += 1
        if self.i == 1:
            return self.first
        if self.i == 2:
            return self.first
        if self.i == 3:
            return self.first
        if self.i == 4:
            return 'Подсчет окончен'
        raise StopIteration()  # признак того, что больше возвращать нечего


obj = Iter()
print(obj)

for value in obj:
    print(value)


def fibonacci(n):
    result = []
    a = 0
    b = 1
    for i in range(n):
        result.append(a)
        a, b = b, a+b
    return result


print(fibonacci(10))


class Fibonacci:
    def __init__(self, n):
        self.i = 0
        self.a = 0
        self.b = 1
        self.n = n

    def __iter__(self):
        self.i = 0  # обнулили счетчик
        self.a = 0
        self.b = 1
        return self  # возвращаем ссылку на себя, чтобы объект класса стал итератором

    def __next__(self):  # метод возвращает значение по требованию python, ленивое вычислениt
        self.i += 1
        if self.i > 1:
            if self.i > self.n:
                raise StopIteration
            else:
                self.a, self.b = self.b, self.a + self.b
        return self.a


fib = Fibonacci(20)
print(fib)
for value in fib:
    print(value)

