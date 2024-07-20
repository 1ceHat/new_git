from runner import Runner
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        test_runner = Runner('F')

        for _ in range(10):
            test_runner.walk()

        self.assertEqual(test_runner.distance, 50)

    def test_run(self):
        test_runner = Runner('F')

        for _ in range(10):
            test_runner.run()

        self.assertEqual(test_runner.distance, 100)

    def test_challenge(self):
        test_runner1 = Runner('F')
        test_runner2 = Runner('G')

        for _ in range(10):
            test_runner1.run()
            test_runner2.walk()

        self.assertNotEqual(test_runner1.distance, test_runner2)


if __name__ == "__main__":

    unittest.main()