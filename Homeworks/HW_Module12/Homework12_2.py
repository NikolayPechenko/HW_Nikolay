import runner_and_tournament
import unittest
import pprint


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    def setUp(self):
        self.andrey = runner_and_tournament.Runner('Andrey', 9)
        self.usain = runner_and_tournament.Runner('Usain', 10)
        self.nick = runner_and_tournament.Runner('Nick', 3)

    @classmethod
    def tearDownClass(cls):
        pprint.pprint(cls.all_result)

    def test1(self):
        a = runner_and_tournament.Tournament(90, self.usain,  self.nick)
        TournamentTest.all_result[1] = a.start()
        b = TournamentTest.all_result[1].keys()
        self.assertTrue(TournamentTest.all_result[1][max(b)] == 'Nick')

    def test2(self):
        a = runner_and_tournament.Tournament(90, self.andrey, self.nick)
        TournamentTest.all_result[2] = a.start()
        b = TournamentTest.all_result[2].keys()
        self.assertTrue(TournamentTest.all_result[2][max(b)] == 'Nick')

    def test3(self):
        a = runner_and_tournament.Tournament(90, self.usain, self.andrey, self.nick)
        TournamentTest.all_result[3] = a.start()
        b = TournamentTest.all_result[3].keys()
        self.assertTrue(TournamentTest.all_result[3][max(b)] == 'Nick')

    def test4(self):
        r = runner_and_tournament.Tournament(1, self.nick, self.andrey, self.usain)
        TournamentTest.all_result[4] = r.start()
        b = TournamentTest.all_result[4].keys()
        self.assertTrue(TournamentTest.all_result[4][max(b)] == 'Nick')

