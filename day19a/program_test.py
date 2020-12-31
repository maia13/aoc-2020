import unittest
from program_lib import calculate

class AcronymTest(unittest.TestCase):
    def test_calculate_data(self):
        # too high 2097152
        self.assertEqual(calculate("data.txt", 129), 171)

    # def test_calculate_example1(self):
    #     self.assertEqual(calculate("data_example1.txt", 4), 2)

    def test_calculate_example2(self):
        self.assertEqual(calculate("data_example2.txt", 6), 2)

    # def test_calculate_example3(self):
    #     self.assertEqual(calculate("data_example3.txt", 7), 24)
if __name__ == "__main__":
    unittest.main()