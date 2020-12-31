import unittest
from program_lib import calculate

class AcronymTest(unittest.TestCase):
    def test_calculate_685974213_100(self):
        self.assertEqual(calculate("685974213", 100), "82635947")

    def test_calculate_389125467_10(self):
        self.assertEqual(calculate("389125467", 10), "92658374")

    def test_calculate_389125467_100(self):
        self.assertEqual(calculate("389125467", 100), "67384529")

if __name__ == "__main__":
    unittest.main()