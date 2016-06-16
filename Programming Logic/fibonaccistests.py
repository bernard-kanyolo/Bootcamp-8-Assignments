import unittest
from fibonaccis import nth_fib


class NthFibonacciTestCases(unittest.TestCase):
    """unit tests for fibonacci numbers from 0 to n
    """

    def test_lower_edge(self):
        """test lower edge case
        """

        self.assertListEqual(nth_fib(-1), [],
                             msg='An input < 0 should return the empty list')
        self.assertListEqual(nth_fib(0), [0],
                             msg='The fib number from 0 to 0 is only 0')

    def test_normal_behaviour(self):
        """test a few random values for correctness
        """

        self.assertListEqual(nth_fib(1), [0, 1, 1],
                             msg='The fib numbers from 0 to 1 are 0,1,1')
        self.assertListEqual(nth_fib(2), [0, 1, 1, 2],
                             msg='The fib numbers from 0 to 2 are 0,1,1,2')
        self.assertListEqual(nth_fib(10), [0, 1, 1, 2, 3, 5, 8],
                             msg='The fib numbers from 0 to 10 are incorrect')
        self.assertListEqual(nth_fib(20), [0, 1, 1, 2, 3, 5, 8, 13],
                             msg='The fib numbers from 0 to 10 are incorrect')

    def test_invalid_input(self):
        """test that input is properly validated
        """
        self.assertEqual(nth_fib(""), 'invalid input',
                         msg='A string should return an error message')
        self.assertEqual(nth_fib({}), 'invalid input',
                         msg='A dictionary should return an error message')
        self.assertEqual(nth_fib([]), 'invalid input',
                         msg='A list should return an error message')

    def test_large_number(self):
        """test what happens when a relatively large number is used
        """
        self.assertListEqual(nth_fib(100),
                             [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
                             msg='The fib numbers from 0 to 10 are incorrect')

if __name__ == '__main__':
    unittest.main()
