import unittest
import Homework12_1
import Homework12_2

runnerTS = unittest.TestSuite()
runnerTS.addTest(unittest.TestLoader().loadTestsFromTestCase(Homework12_1.RunnerTest))
runnerTS.addTest(unittest.TestLoader().loadTestsFromTestCase(Homework12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runnerTS)