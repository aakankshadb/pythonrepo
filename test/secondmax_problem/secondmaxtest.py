import unittest
from src.secondmax_problem.utils import *


class MyTestCase(unittest.TestCase):
    def test_something1(self):
        n=5
        test_lis=[2,3,6,6,5]
        actualoutput=second_max(n,test_lis)
        expectedoutput=5
        self.assertEqual(actualoutput,expectedoutput)  # testcase1

    def test_something2(self):
        n=7
        test_lis=[4,7,8,3,10,5,7]
        actualoutput=second_max(n,test_lis)
        expectedoutput=8
        self.assertEqual(actualoutput,expectedoutput)  # testcase2


if __name__ == '__main__':
    unittest.main()
