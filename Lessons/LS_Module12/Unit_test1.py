import calc
import unittest


class Calctest(unittest.TestCase):
    def setUp(self):  # запускается перед каждым тест кейсом
        print('setUp')

    @classmethod
    def setUpClass(cls):  # запускается один раз перед тест кейсами
        print('MegasetUp')

    def tearDown(self):  # аналогично в конце
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(calc.sub(5, 3), 2)

    def test_mul(self):
        self.assertEqual(calc.mul(9, 5), 45)

    def test_div(self):
        self.assertEqual(calc.div(14, 2), 7)


if __name__ == '__main__':
    unittest.main()