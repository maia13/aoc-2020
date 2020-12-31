import unittest
from program_lib import calculate, combine_rules

class AcronymTest(unittest.TestCase):

    # srule: [4, ['ab', 'bb'], True]
    # urule: [2, [(4, 4), (5, 5)], False]
    def test_combine_rules1(self):
        urule = [[4, 4], [5, 5]]
        srule = ['ab', 'bb']
        sid = 4
        self.assertEqual(combine_rules(sid, srule, urule), ['abab', 'abbb', 'bbab', 'bbbb', [5, 5]])

    def test_combine_rules2(self):
        urule = [[4, 7], [5, 5]]
        srule = ['ab', 'bb']
        sid = 4
        self.assertEqual(combine_rules(sid, srule, urule), [['ab', 7], ['bb', 7], [5, 5]])

    def test_combine_rules3(self):
        urule = [[4, 7], [5, 5]]
        srule = ['ab']
        sid = 4
        self.assertEqual(combine_rules(sid, srule, urule), [['ab', 7], [5, 5]])

    def test_combine_rules4(self):
        urule = [[4, 4], [5, 5]]
        srule = ['ab']
        sid = 4
        self.assertEqual(combine_rules(sid, srule, urule), ['abab', [5, 5]])

    def test_combine_rules5(self):
        urule = [[4, 4], [5, 5]]
        srule = ['ab']
        sid = 3
        self.assertEqual(combine_rules(sid, srule, urule), [[4, 4], [5, 5]])

if __name__ == "__main__":
    unittest.main()