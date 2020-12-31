import unittest
from program_lib import calculate

class AcronymTest(unittest.TestCase):
    def test_calculate_data(self):
        self.assertEqual(calculate([1,2,16,19,18,0], 2020), 536)

    def test_calculate_example1(self):
        self.assertEqual(calculate([0,3,6], 2020), 436)

    # def test_calculate_example2(self):
    #     self.assertEqual(calculate([0,3,6], 30000000), 175594)

    def test_calculate_example3(self):
        self.assertEqual(calculate([1,2,16,19,18,0], 30000000), 24065124)

if __name__ == "__main__":
    unittest.main()