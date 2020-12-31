import unittest
from program_lib import calculate, move_line, get_movement_hash

class AcronymTest(unittest.TestCase):
    def test_calculate_data(self):
        self.assertEqual(calculate("data.txt"), 373)

    def test_calculate_example1(self):
        self.assertEqual(calculate("data_example1.txt"), 10)

    def test_calculate_example2(self):
        self.assertEqual(calculate("data_example2.txt"), 1)

    def test_move_line1(self):
        movement_hash = get_movement_hash()
        self.assertEqual(move_line(movement_hash, "nwwswee", (0, 0)), (0, 0))
    
    def test_move_line2(self):
        movement_hash = get_movement_hash()
        self.assertEqual(move_line(movement_hash, "nwwswee", (0, 1)), (0, 1))

    def test_move_line3(self):
        movement_hash = get_movement_hash()
        self.assertEqual(move_line(movement_hash, "nwwswee", (-1, 0)), (-1, 0))

    def test_move_line4(self):
        movement_hash = get_movement_hash()
        self.assertEqual(move_line(movement_hash, "nwwswee", (0, -1)), (0, -1))

    def test_move_line5(self):
        movement_hash = get_movement_hash()
        self.assertEqual(move_line(movement_hash, "nwwswee", (1, -1)), (1, -1))

if __name__ == "__main__":
    unittest.main()