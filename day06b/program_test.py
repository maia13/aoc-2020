

import unittest
from program_lib import calculate, order_number, person_binary, group_sum

class AcronymTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(calculate(), 3351)

    def test_order_number_a(self):
        self.assertEqual(order_number('a'), 0)

    def test_order_number_c(self):
        self.assertEqual(order_number('c'), 2)

    def test_order_number_z(self):
        self.assertEqual(order_number('z'), 25)
    
    def test_person_binary_abc(self):
        self.assertEqual(person_binary('abc'), 1+2+4)

    def test_person_binary_abf(self):
        self.assertEqual(person_binary('abf'), 1+2+32)

    def test_group_sum_abcdef(self):
        self.assertEqual(group_sum(['ab', 'cdef']), 0)

    def test_group_sum_intersect(self):
        self.assertEqual(group_sum(['abf', 'abcdrf']), 3)

    def test_group_sum_alot(self):
        self.assertEqual(group_sum(['wdcmlzfnugqtvjbsahi', 'easrkmocxbpjgi']), 8)

    def test_group_sum_alot2(self):
        self.assertEqual(group_sum(['xrpnegqlcsyodhjfutzakmiwvb', 'mgilapxjtrndbheyqzckfouwsv']), 26)

if __name__ == "__main__":
    unittest.main()
