import unittest
from program_lib import calculate

class AcronymTest(unittest.TestCase):
    def test_calculate_data(self):
        self.assertEqual(calculate("data.txt", 504, 14144619), 1766397)

    def test_calculate_example1(self):
        self.assertEqual(calculate("data_example1.txt", 14, 127), 62)

    # def test_calculate_example2(self):
    #     self.assertEqual(calculate("data_example2.txt"), 0)
if __name__ == "__main__":
    unittest.main()