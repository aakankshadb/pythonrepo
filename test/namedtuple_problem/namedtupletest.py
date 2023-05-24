import unittest
from src.namedtuple_problem.utils import *
class MyTestCase(unittest.TestCase):
    def test_something(self):
        students_data = ['3', 'name mark', 'John 80', 'Emily 90', 'Michael 75']
        actualinput=calculate_average_mark(students_data)
        expectedoutput='81.67'
        self.assertEqual(actualinput, expectedoutput)


if __name__ == '__main__':
    unittest.main()