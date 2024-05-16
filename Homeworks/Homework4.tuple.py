immutable_var = (1,2,True,'Привет')
print(immutable_var)

# immutable_var [0] = 7
# immutable_var [3] = 'Hello'
# print(immutable_var)
# Кортеж является неизменямой коллекцией и не поддерживает обращение по элементам

mutable_list = ['футбол','теннис','хоккей',',баскетбол']
mutable_list[0] = 'ногомяч'
mutable_list.append(2018)
print(mutable_list)

