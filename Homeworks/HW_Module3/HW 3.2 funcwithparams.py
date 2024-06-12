def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(7)
print_params(7, 5)
print_params(False, 12, 'Third')
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, 'строка', True]
values_dict = {'a': 8, 'b': 'Solo', 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['Sochi', 52]
print_params(*values_list_2, 42)
