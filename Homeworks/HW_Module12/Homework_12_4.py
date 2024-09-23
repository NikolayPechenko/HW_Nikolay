import logging
import unittest
import rt_with_exceptions


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            john = rt_with_exceptions.Runner('John', -50)
            for i in range(10):
                john.walk()
            self.assertEqual(john.distance, 50)
            logging.info(f'"test_walk" выполнен успешно')
        except:
            logging.warning(f'Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            john = rt_with_exceptions.Runner(50)
            for i in range(10):
                john.run()
            self.assertEqual(john.distance, 100)
            logging.info(f'"test_run" выполнен успешно')
        except:
            logging.warning(f'Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        bob = rt_with_exceptions.Runner('Bob')
        shisha = rt_with_exceptions.Runner('Shisha')
        for i in range(10):
            bob.walk()
        for i in range(10):
            shisha.run()
        self.assertNotEqual(bob.distance, shisha.distance)


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                    format='%(asctime)s | %(levelname)s |  %(message)s')

