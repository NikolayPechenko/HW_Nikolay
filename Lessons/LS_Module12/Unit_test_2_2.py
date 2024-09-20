import calc
import unittest


class Calctest(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(calc.sqrt(16), 4)

    def test_pow(self):
        self.assertEqual(calc.pow(2, 3), 8)