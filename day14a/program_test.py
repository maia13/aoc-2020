import unittest
from program_lib import calculate, apply_mask

class AcronymTest(unittest.TestCase):
    def test_calculate_data(self):
        self.assertEqual(calculate("data.txt"), 2346881602152)

    def test_calculate_example1(self):
        self.assertEqual(calculate("data_example1.txt"), 165)

    def test_get_mask1(self):
        self.assertEqual(apply_mask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", 11), 73)

    def test_get_mask2(self):
        self.assertEqual(apply_mask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", 101), 101)

    def test_get_mask3(self):
        self.assertEqual(apply_mask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", 0), 64)

if __name__ == "__main__":
    unittest.main()