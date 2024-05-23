def say_hello():
    print('Hello world')

say_hello()


def say_hello(name):
    print('Hello,', name)


say_hello('Nikolay')
say_hello('Anton')

import random
def lottery():
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    win = random.choice(tickets)
    return win


win_number = lottery() ** 2
print(win_number)

import random
def lottery(mon, tue):
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    win1 = random.choice(tickets)
    tickets.remove(win1)
    win2 = random.choice(tickets)
    print(mon, tue)
    return win1, win2


win1, win2 = lottery('ман', 'тью')
print(win1, win2)

import random
def lottery(*arty, **kwargs):
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    win1 = random.choice(tickets)
    tickets.remove(win1)
    win2 = random.choice(tickets)
    print(*arty)
    return win1, win2


win1, win2 = lottery(1, 2, 3, 4, 5, 6, 7, 8)
print(win1, win2)



def test(a = 2, b = True):
    print(a, b)
test()

def test(a = 2, b = True, c = 'Fake'):
    print(a, b, c)
test(*[1,2],1)

def test(a = 2, b = True, c = 'Fake'):
    print(a, b, c)
test(**{'a': 1, 'b': 3, 'c': 5})


def fun(p):
    print(p)


my_dict = {'1': 2, '2': 3, '3': 4}
fun(my_dict)

def fun(p='5', b=5):
    print(p, b)


my_dict = {'p': 2, 'b': 3}
fun(**my_dict)

