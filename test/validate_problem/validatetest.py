import unittest
from src.validate_problem.utils import *

class TestValidateEmail(unittest.TestCase):

    def test_valid_email(self):
        email = 'user@example.com'
        result = validate_email(email)
        self.assertTrue(result)




if __name__ == '__main__':
    unittest.main()
