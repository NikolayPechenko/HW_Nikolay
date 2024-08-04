def is_prime(func):
    def wrapper(*args):
        s = 0
        result = func(*args)
        for i in range(2, result):
            if result % i == 0:
                s += 1
        if s == 0:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


resulted = sum_three(2, 3, 6)
print(resulted)
