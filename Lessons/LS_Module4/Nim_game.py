from nim_engine import put_stones, take_from_bunch, is_game_over, get_bunches
from colorama import init, Fore

put_stones()
user_number = 1


while True:
    print(Fore.BLUE + 'Текущая позиция')
    print(Fore.YELLOW, get_bunches())
    if user_number == 1:
        print(Fore.MAGENTA + 'Ход игрока', user_number)
    else:
        print(Fore.WHITE + 'Ход игрока', user_number)
    pos = int(input(Fore.GREEN + 'Откуда берем? '))
    qua = int(input('Сколько берем? '))
    while True:
        if take_from_bunch(position=int(pos-1), quantity=int(qua)) != 'again':
            break
        else:
            print(Fore.YELLOW + 'Переделывай')
            print(get_bunches())
            print('Ход игрока номер', user_number)
            pos = int(input('Откуда берем? '))
            qua = int(input('сколько берем? '))
    if is_game_over():
        print(Fore.WHITE + 'Выиграл игрок номер', user_number)
        break
    if user_number == 1:
        user_number = 2
    else:
        user_number = 1
