import unittest
from program_lib import calculate

class AcronymTest(unittest.TestCase):
    def test_calculate_data(self):
        self.assertEqual(calculate("data.txt", 25), 14144619)

    def test_calculate_example1(self):
        self.assertEqual(calculate("data_example1.txt", 5), 127)

    # def test_calculate_example2(self):
    #     self.assertEqual(calculate("data_example2.txt"), 0)
if __name__ == "__main__":
    unittest.main()