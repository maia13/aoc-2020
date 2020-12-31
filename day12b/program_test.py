import unittest
from program_lib import *

class AcronymTest(unittest.TestCase):
    def test_calculate_data(self):
        self.assertEqual(calculate("data.txt"), 23960)

    def test_calculate_example1(self):
        self.assertEqual(calculate("data_example1.txt"), 286)

    # [1, 2] -> [2, -1] -> [-1, -2] -> [-2, 1]
    def test_rotate_r_90a(self):
        self.assertEqual(r(90, 0, 0, 1, 2), (0, 0, 2, -1))
    def test_rotate_r_90b(self):
        self.assertEqual(r(90, 0, 0, 2, -1), (0, 0, -1, -2))
    def test_rotate_r_90c(self):
        self.assertEqual(r(90, 0, 0, -1, -2), (0, 0, -2, 1))
    def test_rotate_r_90d(self):
        self.assertEqual(r(90, 0, 0, -2, 1), (0, 0, 1, 2))
    def test_rotate_r_180a(self):
        self.assertEqual(r(180, 0, 0, 1, 2), (0, 0, -1, -2))
    def test_rotate_r_180b(self):
        self.assertEqual(r(180, 0, 0, 2, -1), (0, 0, -2, 1))
    def test_rotate_r_270a(self):
        self.assertEqual(r(270, 0, 0, 1, 2), (0, 0, -2, 1))
    def test_rotate_r_270b(self):
        self.assertEqual(r(270, 0, 0, -1, -2), (0, 0, 2, -1))
    def test_rotate_l_90a(self):
        self.assertEqual(l(90, 0, 0, 1, 2), (0, 0, -2, 1))
    def test_rotate_l_90b(self):
        self.assertEqual(l(90, 0, 0, 2, -1), (0, 0, 1, 2))
    def test_rotate_l_90c(self):
        self.assertEqual(l(90, 0, 0, -1, -2), (0, 0, 2, -1))
    def test_rotate_l_90d(self):
        self.assertEqual(l(90, 0, 0, -2, 1), (0, 0, -1, -2))

    # The waypoint starts 10 units east and 1 unit north relative to the ship.
    # F10 moves the ship to the waypoint 10 times (a total of 100 units east and 10 units north), 
    # leaving the ship at east 100, north 10. The waypoint stays 10 units east and 1 unit north of the ship.
    def test_fa(self):
        self.assertEqual(f(10, 0, 0, 10, 1), (100, 10, 10, 1))
    # Waypoint is 10 units east and 4 units north of the ship. The ship remains at east 100, north 10.
    # F7 moves the ship to the waypoint 7 times (a total of 70 units east and 28 units north), 
    # leaving the ship at east 170, north 38. The waypoint stays 10 units east and 4 units north of the ship.
    def test_fb(self):
        self.assertEqual(f(7, 100, 10, 10, 4), (170, 38, 10, 4))
    # Waypoint is 4 units east and 10 units south of the ship. The ship remains at east 170, north 38
    # F11 moves the ship to the waypoint 11 times (a total of 44 units east and 110 units south), 
    # leaving the ship at east 214, south 72. The waypoint stays 4 units east and 10 units south of the ship.
    def test_fc(self):
        self.assertEqual(f(11, 170, 38, 4, -10), (214, -72, 4, -10))

    
if __name__ == "__main__":
    unittest.main()