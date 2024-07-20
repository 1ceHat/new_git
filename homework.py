from runner import Runner
import unittest
import logging

class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            test_runner = Runner('F')

            for _ in range(10):
                test_runner.walk()
            logging.info('"test_walk" выполнен успешно!')
            self.assertEqual(test_runner.distance, 50)
        except ValueError as e:
            logging.warning(e)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            test_runner = Runner(2)

            for _ in range(10):
                test_runner.run()

            logging.info('"test_run" выполнен успешно!')
            self.assertEqual(test_runner.distance, 100)
        except TypeError as e:
            logging.warning(e)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test_runner1 = Runner('F')
        test_runner2 = Runner('G')

        for _ in range(10):
            test_runner1.run()
            test_runner2.walk()

        self.assertNotEqual(test_runner1.distance, test_runner2)


logging.basicConfig(level=logging.INFO, filemode="w", filename='runner_test1.log', encoding="utf-8",
                    format="%(asctime)s || %(levelname)s || %(message)s")

if __name__ == "__main__":
    unittest.main()

