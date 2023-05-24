import unittest
import src.meanvarstd_problem.utils as f
import numpy as np

class MyTestCase(unittest.TestCase):
    def test_mean(self):
        test_array=([1,2],[3,4])
        actualoutput=f.mean_func(test_array)
        expectedoutput=np.array([1.5,3.5])
        self.assertIsNone(np.testing.assert_almost_equal(actualoutput,expectedoutput,1))  # add assertion here
    def test_var(self):
        test_array = ([1, 2],[3, 4])
        actualoutput =f.var_func(test_array)
        expectedoutput =np.array([1,1])
        self.assertIsNone(np.testing.assert_almost_equal(actualoutput,expectedoutput,1))  # add assertion here
    def test_std(self):
        test_array = ([1, 2],[3, 4])
        actualoutput =f.std_func(test_array)
        expctedoutput =1.11803398875
        self.assertEqual(actualoutput,expctedoutput)  # add assertion here


if __name__ == '__main__':
    unittest.main()
