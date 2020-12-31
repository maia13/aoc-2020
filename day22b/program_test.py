import unittest
from program_lib import calculate

class AcronymTest(unittest.TestCase):
    def test_calculate_data(self):
        self.assertEqual(calculate("data.txt"), 31120)

    def test_calculate_example1(self):
        self.assertEqual(calculate("data_example1.txt"), 291)

    # possible forever loop
    def test_calculate_example2(self):
        self.assertEqual(calculate("data_example2.txt"), 105)
if __name__ == "__main__":
    unittest.main()