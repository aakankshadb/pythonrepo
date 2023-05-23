import unittest
from src.mutation_problem.utils import *


class MyTestCase(unittest.TestCase):
    def test_something1(self):
        test_string="Sunny"
        test_position=0
        test_character="B"
        actualoutput=mutate_string(test_string,test_position,test_character)
        expectedoutput="Bunny"
        self.assertEqual(actualoutput,expectedoutput)  # testcase1
    def test_something2(self):
        test_string="Rosh"
        test_position=3
        test_character="y"
        actualoutput=mutate_string(test_string,test_position,test_character)
        expectedoutput="Rosy"
        self.assertEqual(actualoutput,expectedoutput)  # testcase1


if __name__ == '__main__':
    unittest.main()
