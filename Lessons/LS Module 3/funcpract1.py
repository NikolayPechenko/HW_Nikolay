# def find_max(list_):
#     max_ = list_[0]
#     for i in list_:
#         if i > max_:
#             max_ = i
#     return max_
#
# a = [0,1,2,3,4,5,-1.5]
# print(find_max(a))


# def count_even(list_):
#     count_ = 0
#     for i in list_:
#         if i % 2 == 0:
#             count_ = count_ + 1
#     return count_
#
#
# a = [0,1,2,3,4,5,-1.5]
# print(count_even(a))


def unic_spisok(list_):
    spisok = []
    for i in list_:
        if i not in spisok:
            spisok.append(i)
    return spisok


a = [0,0,1,2,2,3,4,5,-1.5]
print(unic_spisok(a))

