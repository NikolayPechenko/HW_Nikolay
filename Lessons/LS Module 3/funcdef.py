# def print_params(a, b, c):
#     print(a, b, c)
#
#
# print_params(1, 2, 3)
# print_params(True, 'True', 3)


def print_params(a=1, b=2, c=3):
    print(a, b, c)


print_params()
print_params(6,2, c='String')  #позиционный параметр перед именованным
print_params()