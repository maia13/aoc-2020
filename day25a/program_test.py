import unittest
from program_lib import calculate, transform, find_loopsize

class AcronymTest(unittest.TestCase):
    def test_calculate_data(self):
        self.assertEqual(calculate("data.txt"), 18329280)

    def test_calculate_example1(self):
        self.assertEqual(calculate("data_example1.txt"), 14897079)

    def test_loopsize8(self):
        self.assertEqual(find_loopsize(7, 5764801), 8)

    def test_loopsize11(self):
        self.assertEqual(find_loopsize(7, 17807724), 11)

    def test_transform7_8(self):
        self.assertEqual(transform(7, 8), 5764801)

    def test_transform7_11(self):
        self.assertEqual(transform(7, 11), 17807724)

    def test_transform17807724_8(self):
        self.assertEqual(transform(17807724, 8), 14897079)

    def test_transform5764801_11(self):
        self.assertEqual(transform(5764801, 11), 14897079)

if __name__ == "__main__":
    unittest.main()