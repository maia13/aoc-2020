import unittest
from program_lib import calculate, eval_expression

class AcronymTest(unittest.TestCase):
    def test_calculate_data(self):
        self.assertEqual(calculate("data.txt"), 31142189909908)

    def test_calculate_example1(self):
        self.assertEqual(eval_expression("1 + 2 * 3 + 4 * 5 + 6"), 71)

    def test_calculate_example7(self):
        self.assertEqual(eval_expression("(1 + 2 * 3 + 4 * 5 + 6)"), 71)

    def test_calculate_example8(self):
        self.assertEqual(eval_expression("((1 + 2 * 3 + 4 * 5 + 6))"), 71)

    def test_calculate_example2(self):
        self.assertEqual(eval_expression("1 + (2 * 3) + (4 * (5 + 6))"), 51)

    def test_calculate_example3(self):
        self.assertEqual(eval_expression("2 * 3 + (4 * 5)"), 26)

    def test_calculate_example4(self):
        self.assertEqual(eval_expression("5 + (8 * 3 + 9 + 3 * 4 * 3)"), 437)

    def test_calculate_example5(self):
        self.assertEqual(eval_expression("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"), 12240)

    def test_calculate_example6(self):
        self.assertEqual(eval_expression("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"), 13632)
if __name__ == "__main__":
    unittest.main()