def check_winner():
    return 'XXX'
    # if area[0][0] == 'X' and area[0][1] and area[0][2] == 'X':
    #     return 'X'
    # if area[0][0] == 'X' and area[0][1] and area[0][2] == 'X':
    #     return 'X'
    # if area[0][0] == 'X' and area[0][1] and area[0][2] == 'X':
    #     return 'X'
    # .....
    #  else:
    #     return 'C'

#
#
#
#
#
#
#
#
#
#
def draw_area():
    for i in area:
        print(*i)
    print()


# area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
# print('Привествую тебя в моей первой игрульке')
# print('--------------------------------------')
# draw_area()
# for turn in range (1,10):
#     print (f'Ход номер: {turn}')
#     if turn % 2 == 0:
#         turn_char = '0'
#         print('Ходят нолики')
#     else:
#         turn_char = 'X'
#         print('Ходят крестики')
#     row = int(input('Введите номер строки (1,2,3) ')) - 1
#     column = int(input('Введите номер столбца (1,2,3) ')) - 1
#     if area[row][column] == '*':
#         area[row][column] = turn_char
#     else:
#         print('Ячейка уже занята, пропускаете ход')
#         draw_area()
#         continue
#     draw_area()



area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
print('Привествую тебя в моей первой игрульке')
print('--------------------------------------')
draw_area()
# while True:
#     if c
#         break
#
#     print (f'Ход номер: {turn}')
#     if turn % 2 == 0:
#         turn_char = '0'
#         print('Ходят нолики')
#     else:
#         turn_char = 'X'
#         print('Ходят крестики')
#     row = int(input('Введите номер строки (1,2,3) ')) - 1
#     column = int(input('Введите номер столбца (1,2,3) ')) - 1
#     if area[row][column] == '*':
#         area[row][column] = turn_char
#     else:
#         print('Ячейка уже занята, пропускаете ход')
#         draw_area()
#         continue
#     draw_area()

def is_game_complited():
    return False
def game():
    turn = 1
    while True:
        result = check_winner()
        if result == 'C':
            break
        print (f'Ход номер: {turn}')
        if turn % 2 == 0:
            turn_char = '0'
            print('Ходят нолики')
        else:
            turn_char = 'X'
            print('Ходят крестики')
        row = int(input('Введите номер строки (1,2,3) ')) - 1
        column = int(input('Введите номер столбца (1,2,3) ')) - 1
        if area[row][column] == '*':
            area[row][column] = turn_char
            turn += 1
            draw_area()
        else:
            draw_area()
            print('Переделывай, долбаеб')
game()
