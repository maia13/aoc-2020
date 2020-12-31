import unittest
from program_lib import calculate

class AcronymTest(unittest.TestCase):
    def test_calculate(self):
        self.assertEqual(calculate(), 213)

if __name__ == "__main__":
    unittest.main()