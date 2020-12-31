import unittest
from program_lib import calculate

class AcronymTest(unittest.TestCase):
    def test_calculate_data(self):
        self.assertEqual(calculate("data.txt"), 4315)

    def test_calculate_example1(self):
        self.assertEqual(calculate("data_example1.txt"), 295)

if __name__ == "__main__":
    unittest.main()