import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        john = runner.Runner('John')
        for i in range(10):
            john.walk()
        self.assertEqual(john.distance, 50)

    def test_run(self):
        john = runner.Runner('John')
        for i in range(10):
            john.run()
        self.assertEqual(john.distance, 100)

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