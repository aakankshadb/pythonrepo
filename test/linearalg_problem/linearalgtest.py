import unittest
from src.linearalg_problem.utils import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        test_array=([1.1,1.1],[1.1,1.1])
        actualoutput=determinant(test_array)
        expectedoutput=0.0
        self.assertEqual(actualoutput,expectedoutput)  # add assertion here


if __name__ == '__main__':
    unittest.main()
