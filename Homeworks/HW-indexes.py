name = 'это моя строка'
print(name[0])
print(name[-1])
print(name[2:5])
print(name[::-1])
print(len(name))
print(name+name)

name = 'Сейчас на Земле появился новый вид роботов. Раньше их называли „железной оравой “, но это не очень точное определение'
print (name.split('.')[0])

name = 'радар'
print(name[::-1])
name = 'норма'
print(name[::-1])

name = 'кенгуру'
hl = len(name) // 2 + len(name) % 2
print(name[hl:]+name[:hl])

name = 'нейропрограммирование'
print(name[::2],name[1::2])

name = 'нейропластичность'
print(name[len(name)-2:0:-1])
print(name[-2:-len(name):-1])

