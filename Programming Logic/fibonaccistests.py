import unittest
from fibonaccis import nth_fib


class NthFibonacciTestCases(unittest.TestCase):

    def test_lower_edge(self):
        self.assertEqual(nth_fib(0), 'invalid input',
                         msg='An input of zero should return an error message')
        self.assertEqual(nth_fib(-1), 'invalid input',
                         msg='An input < 0 should return an error message')

    def test_normal_behaviour(self):
        self.assertEqual(nth_fib(1), 0, msg='The first fib number is 0')
        self.assertEqual(nth_fib(2), 1,
                         msg='The second fib number is 1')
        self.assertEqual(nth_fib(10), 34,
                         msg='The tenth fib number is 34')

    def test_invalid_input(self):
        self.assertEqual(nth_fib(""), 'invalid input',
                         msg='A string should return an error message')
        self.assertEqual(nth_fib({}), 'invalid input',
                         msg='A dictionary should return an error message')

if __name__ == '__main__':
    unittest.main()
