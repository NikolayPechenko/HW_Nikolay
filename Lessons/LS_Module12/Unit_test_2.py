import calc
import unittest
import random

a = random.randint(0, 3)


class Calctest(unittest.TestCase):
    @unittest.skip('Не нравится')  # пропустили тест
    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)

    @unittest.skipIf(a > 1, 'Не повзело')  # пропускаем при условии
    def test_sub(self):
        self.assertEqual(calc.sub(5, 3), 2)

    def test_mul(self):
        self.assertEqual(calc.mul(9, 5), 45)

    def test_div(self):
        self.assertEqual(calc.div(14, 2), 7)


print(a)
