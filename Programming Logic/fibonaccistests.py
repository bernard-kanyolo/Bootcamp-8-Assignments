import unittest
from fibonaccis import fib_to


class NthFibonacciTestCases(unittest.TestCase):
    """unit tests for fibonacci numbers from 0 to n
    """

    def test_lower_edge_less_than_0(self):
        """test lower edge case < 0
        """
        self.assertListEqual(fib_to(-1), [],
                             msg='An input < 0 should return the empty list')

    def test_lower_edge_zero(self):
        """test lower edge of 0
        """
        self.assertListEqual(fib_to(0), [],
                             msg='An input of 0 should return the empty list')

    def test_fib_one_is_zero(self):
        """test normal functionality fib 1
        """
        self.assertListEqual(fib_to(1), [0],
                             msg='The first fib number is 0')

    def test_normal_functionality_2(self):
        """test for fib_to 2
        """
        self.assertListEqual(fib_to(2), [0, 1],
                             msg='The first two fib numbers are 0,1')

    def test_normal_functionality_10(self):
        """test for fib_to 10
        """
        self.assertListEqual(fib_to(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34],
                             msg='The first 10 fib numbers are incorrect')

    def test_normal_functionality_7(self):
        """test for fib_to 7
        """
        self.assertListEqual(fib_to(7), [0, 1, 1, 2, 3, 5, 8],
                             msg='The first 7 fib numbers are incorrect')

    def test_invalid_input_string(self):
        """test that string input isn't accepted
        """
        self.assertEqual(fib_to(""), 'invalid input',
                         msg='A string should return an error message')

    def test_invalid_input_dict(self):
        """test that dict input isn't accepted
        """
        self.assertEqual(fib_to({}), 'invalid input',
                         msg='A dictionary should return an error message')

    def test_invalid_input_list(self):
        """test that list input isn't accepted
        """
        self.assertEqual(fib_to([]), 'invalid input',
                         msg='A list should return an error message')

    def test_large_number(self):
        """test what happens when a relatively large number is used
        """
        nums = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040,
                1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903]
        self.assertListEqual(fib_to(47),
                             nums,
                             msg='The first 47 fib numbers are incorrect')

if __name__ == '__main__':
    unittest.main()
