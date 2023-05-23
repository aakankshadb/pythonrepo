import unittest
from src.calendar_problem.utils import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        actualoutput=calender(8,5,2015)
        expectedoutput='WEDNESDAY'
        self.assertEqual(actualoutput,expectedoutput)  # add assertion here


if __name__ == '__main__':
    unittest.main()
