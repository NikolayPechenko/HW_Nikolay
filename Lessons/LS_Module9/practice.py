animal = 'мишка'
animals = ['зайка', 'микша', 'бегемотик']


def gen_repeat(n):
    def repeat(animal):
        return (animal[0:2] + '-') * n + animal

    return repeat


    #1

test_1 = gen_repeat(2)
print(test_1(animal))

    #2

repetitions = [gen_repeat(n) for n in range(1, 4)]

result = [func(animal) for func in repetitions]
print(result)

    # 3

fin_result = [func(i) for func in repetitions for i in animals]
print(fin_result)


def memoize(f):
    mem = {}
    def wrapper(*args):
        if args not in mem:
            mem[args] = f(*args)
            return f(*args)
        else:
            return f'Функция уже применена, ответ {mem[args]}'
    return wrapper


@memoize
def func(a, b):
    return a ** b


print(func(2, 5))
print(func(2, 4))
print(func(2, 3))
print(func(2, 5))
print(func(2, 4))
print(func(4, 4))
print(func(2, 5))
print(func(4, 2))
