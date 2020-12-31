import unittest
from program_lib import calculate, decode, seat_id

class ProgramTest(unittest.TestCase):
    def test_calculate(self):
        self.assertEqual(calculate(), 955)

    def test_decode_1(self):
        row, col = decode('FBFBBFFRLR')
        self.assertEqual(row, 44)
        self.assertEqual(col, 5)

    def test_seat_id_1(self):
        id = seat_id(70, 7)
        self.assertEqual(id, 567)

    def test_seat_id_2(self):
        id = seat_id(14, 7)
        self.assertEqual(id, 119)

    def test_seat_id_3(self):
        id = seat_id(102, 4)
        self.assertEqual(id, 820)

if __name__ == "__main__":
    unittest.main()

