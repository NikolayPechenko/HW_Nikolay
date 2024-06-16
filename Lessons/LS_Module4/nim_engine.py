from random import randint


_holder = []


def put_stones():  # разложим камни
    global _holder
    _holder = []
    for i in range(3):
        _holder.append(randint(1, 20))



def take_from_bunch(position, quantity):  #  функция, показывающая из какой кучи и сколько камней взято
    if 0 <= (position) <= len(_holder):
        if quantity > _holder[position] or quantity < 1:
            return 'again'
        else:
            _holder[position] = _holder[position] - quantity
    else:
        return 'again'


def get_bunches():  # функция показывающая позиции камней
    return _holder


def is_game_over():
    return sum(_holder) == 0


# put_stones()
# print(_holder)

