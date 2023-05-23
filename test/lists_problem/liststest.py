import unittest
from src.lists_problem.utils import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        n=5
        cmmd=["insert 0 6","insert 1 4","append 9","reverse","print"]
        actualoutput=list_func(n,cmmd)
        expectedoutput=[9,4,6]
        self.assertEqual(actualoutput,expectedoutput)  # add assertion here


if __name__ == '__main__':
    unittest.main()
