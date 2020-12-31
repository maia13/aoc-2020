import unittest
from program_lib import calculate, get_addresses

class AcronymTest(unittest.TestCase):
    def test_calculate_data(self):
        self.assertEqual(calculate("data.txt"), 3885232834169)

    def test_calculate_example1(self):
        self.assertEqual(calculate("data_example1.txt"), 208)

if __name__ == "__main__":
    unittest.main()