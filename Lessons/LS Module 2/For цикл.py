for i in 1,2,3,4:
    print('ok')

for i in 1,2,3,4:
    print(i)

list_ = ['Hello', 'World']
for i in list_:
    print(i)

list_ = ['one', 'two', 'three']
for i in list_:
    print(i)

list_ = ['one', 'two', 'three']
for i in list_:
    if i == 'three':
        list_.remove(i)

print(list_)

list_ = ['one', 'two', 'three']

for i in range(len(list_)):
    list_[i] = 'aa'
print(list_)

List_2 = [2, 3, 4, 5, 1]
sum_ = 0
for i in range(len(List_2)):
    sum_ = sum_ + List_2[i] # (sum_ = sum_ +) = sum_ +=

print(sum_)

for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i} x {j} = {i*j}')

dict_ = {'a': 1, 'b': 3, 'c': 5}
for i in dict_:
    print(i, dict_[i])

dict_ = {'a': 1, 'b': 3, 'c': 5}
for i, j in dict_.items():
    print(i, j)
