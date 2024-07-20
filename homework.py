from runner import Runner, Tournament
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print(result)

    def test_start1(self):
        tour = Tournament(90, self.runner1, self.runner3)
        result = tour.start()
        self.all_results.append(result)
        self.assertTrue(list(result.values())[-1] == 'Ник')

    def test_start2(self):
        tour = Tournament(90, self.runner2, self.runner3)
        result = tour.start()
        self.all_results.append(result)
        self.assertTrue(list(result.values())[-1] == 'Ник')

    def test_start3(self):
        tour = Tournament(90, self.runner1, self.runner2, self.runner3)
        result = tour.start()
        self.all_results.append(result)
        self.assertTrue(list(result.values())[-1] == 'Ник')


if __name__ == "__main__":
    print()
    #unittest.main()