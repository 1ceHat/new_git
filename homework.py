import unittest
import RunnerTest
import TournamentTest

tournamentTestSuit = unittest.TestSuite()

tournamentTestSuit.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest.RunnerTest))
tournamentTestSuit.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(tournamentTestSuit)