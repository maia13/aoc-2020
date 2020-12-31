import unittest
from program_lib import calculate, calc

class AcronymTest(unittest.TestCase):
    def test_calculate_data(self):
        self.assertEqual(calculate(), 38426)

    def test_calculate_example1(self):
        self.assertEqual(calc("data_example1.txt"), 126)

    def test_calculate_example2(self):
        self.assertEqual(calc("data_example2.txt"), 32)

if __name__ == "__main__":
    unittest.main()