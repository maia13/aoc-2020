import unittest
from program_lib import calculate, calc

class AcronymTest(unittest.TestCase):
    # def test_calculate_data(self):
    #     self.assertEqual(calculate("data.txt",100034439999963), 4315)

    def test_calculate_example1(self):
        self.assertEqual(calculate("data_example1.txt", 999999), 1068781)

    def test_calc_3417(self):
        self.assertEqual(calc("17,x,13,19"), 3417)

    def test_calc_754018(self):
        self.assertEqual(calc("67,7,59,61"), 754018)

    def test_calc_779210(self):
        self.assertEqual(calc("67,x,7,59,61"), 779210)

    def test_calc_1261476(self):
        self.assertEqual(calc("67,7,x,59,61"), 1261476)

    def test_calc_1202161486(self):
        self.assertEqual(calc("1789,37,47,1889"), 1202161486)

if __name__ == "__main__":
    unittest.main()