import numpy as np
import requests
import pprint
from bs4 import BeautifulSoup

z = input('Библиотка numpy - введите 1, библиотека request - введите 2 \n')
match z:
    case '1':
        print('библиотека numpy, некоторые методы и функция с ними')
        a = np.array([1, 2, 3, 4, 5, 6])  # создали массив a
        b = a + 1  # созадли массив b, увеличив каждый его элемент на 1
        print(a)
        print(b)
        print(a + b)  # сложили массивы

        c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # создали матрицу, также можно с помощью np.matrix
        print(c)
        print(c.shape)  # вывели размер матрицы
        print(c.sum())  # сумма чисел

        d = np.linspace(2, 32, 3)  # созадли массив d, в котором 3 элемента
        print(d)
        print('-------------------')

        def random_matrix(rows,
                          columns):  # данная функция создает рандомную матрицу и выдает ее минимальное и максимальное значение
            matrix = np.random.rand(rows, columns)
            print(matrix)
            print(matrix.min())  # одна реализация этого метода
            print(np.max(matrix))  # вторая реализация этого метода


        random_matrix(2, 3)
        print('-------------------')

        rows = 3
        cols = 4
        low = 0
        high = 10

        matrix_int = np.random.randint(low, high, size=(rows, cols))  # создали целочисленную матрицу
        print(matrix_int)
        print(np.sum(matrix_int, axis=1))  # посчитали сумма в каждой строке

    case '2':
        x = input('Первый пример - введите 1, второй пример - введите 2 \n')
        match x:
            case '1':
                print('выдержка из книга, красиво оформленная')
                url = 'https://nocover.ru/'
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                text = soup.get_text(separator='\n', strip=True)
                a = text.replace('NoCover.ru — литература без обложки\n', '').replace('\n', '')
                a = a[:-1349]
                pprint.PrettyPrinter().pprint(a)
            case '2':
                print('Просто факт о кошках из интернета')
                url = 'https://catfact.ninja/fact'
                response = requests.get(url)
                print(response.json())

