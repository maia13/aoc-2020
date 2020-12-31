import unittest
from program_lib import calculate

class AcronymTest(unittest.TestCase):
    def test_calculate_685974213_100(self):
        self.assertEqual(calculate("685974213", 100, 9), (8, 2))

    # slow (~ 1 minute)
    def test_calculate_389125467(self):
        self.assertEqual(calculate("389125467", 10000000), (934001, 159792))

    # slow (~ 1 minute)
    def test_calculate_685974213(self):
        self.assertEqual(calculate("685974213", 10000000), (470997, 333437))

if __name__ == "__main__":
    unittest.main()