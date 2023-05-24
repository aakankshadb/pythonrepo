import unittest
from src.noidea_problem.utils import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        test_elements=[1,5,3]
        A={3,1}
        B={5,7}
        actualoutput=happiness_calc(test_elements,A,B)
        expectedoutput=1
        self.assertEqual(actualoutput,expectedoutput)  # add assertion here


if __name__ == '__main__':
    unittest.main()
