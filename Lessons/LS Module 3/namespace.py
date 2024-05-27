a = 5
b = 10
# #
# #
# # def printer():
# #     c = 15
# #     d = 20
# #     print(c, d)
# #
# #
# # print(a, b)
# # printer()


# def printer():
#     a = 19  # a (меняется только для функции)
#     c = 15
#     d = 20
#     print(a, c, d)
#
#
# printer()
# print(a)


def printer():
    global a, b  # меняем глобально
    a = 19
    b = 13
    c = 15
    d = 20
    print(a, b, c, d)


printer()
print(a)
