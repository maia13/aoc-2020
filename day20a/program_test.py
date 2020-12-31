import unittest
from program_lib import calculate

class AcronymTest(unittest.TestCase):
    # 12*12 = 144
    def test_calculate_data(self):
        self.assertEqual(calculate("data.txt"), 45443966642567)

    def test_calculate_example1(self):
        self.assertEqual(calculate("data_example1.txt"), 20899048083289)

if __name__ == "__main__":
    unittest.main()