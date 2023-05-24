import unittest
import src.floorceilrint_problem.utils as f
import numpy as np
class MyTestCase(unittest.TestCase):
    def test_floor(self):
        test_arr= np.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
        result = f.floors(test_arr)
        expected_arr= np.array([1., 2., 3., 4., 5., 6., 7., 8., 9.])
        self.assertIsNone(np.testing.assert_almost_equal(result,expected_arr,1))

    def test_ceil(self):
        test_arr= np.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
        result = f.ceils(test_arr)
        expected_arr= np.array([2.0, 3.0,4.0, 5.0, 6.0, 7.0, 8.0, 9.0,10.0])
        self.assertIsNone(np.testing.assert_almost_equal(result,expected_arr,1))

    def test_rints(self):
        test_arr= np.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
        result = f.rints(test_arr)
        expected_arr= np.array([1.,2., 3.,4., 5., 6., 7., 8., 9.,10.])
        self.assertIsNone(np.testing.assert_almost_equal(result,expected_arr,1))

if __name__ == '__main__':
    unittest.main()
