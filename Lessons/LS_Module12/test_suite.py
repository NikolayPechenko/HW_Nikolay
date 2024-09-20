import unittest
import Unit_test_2
import Unit_test_2_2


calcTS = unittest.TestSuite()
calcTS.addTest(unittest.TestLoader().loadTestsFromTestCase(Unit_test_2.Calctest))  # добавили класс с тестами в тестсьют
calcTS.addTest(unittest.TestLoader().loadTestsFromTestCase(Unit_test_2_2.Calctest))
# аналогично мы можем подгрузить еще один класс тестов в тестсьют, с другими проверками

runner = unittest.TextTestRunner(verbosity=2)  # создали раннер для запуска
runner.run(calcTS)  # запустили
