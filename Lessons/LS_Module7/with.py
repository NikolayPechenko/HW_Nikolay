import io
from pprint import pprint

name = 'textx2.txt'
with open(name, encoding='utf-8') as file:  # сначала пишется действие, потом название, по умолчанию файл открывается в режиме для чтения
    for line in file:
        print(line, end='')  # end переносит по знаку '', чтобы избежаться пустых строк

# как только действие с отступом заканчивается, файл закрывается
