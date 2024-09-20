import runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        john = runner.Runner('John')
        for i in range(10):
            john.walk()
        self.assertEqual(john.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        john = runner.Runner('John')
        for i in range(10):
            john.run()
        self.assertEqual(john.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        bob = runner.Runner('Bob')
        shisha = runner.Runner('Shisha')
        for i in range(10):
            bob.walk()
        for i in range(10):
            shisha.run()
        self.assertNotEqual(bob.distance, shisha.distance)


if __name__ == '__main__':
    unittest.main()