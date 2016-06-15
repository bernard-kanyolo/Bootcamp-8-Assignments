import unittest


def nth_fib(num):
    '''takes a number, num, greater than 0 and returns the numth fibonacci
     number, where the first two terms of the fibonacci sequence are 0 and 1.
    If num is not a valid number or if num is less than 1, it returns the
    string 'invalid input'
    '''
    try:
        num = int(num)
    except:
        return 'invalid input'

    # setting up the first two values
    if num < 1:
        return 'invalid input'
    elif num == 1:
        return 0
    elif num == 2:
        return 1

    # prepare to loop in order to find values > 2
    fibs = [0, 1]
    num -= 2
    last_index = len(fibs) - 1

    # loop until num is 0, each time calculating and appending the next term
    while num:
        last = fibs[last_index]
        second_last = fibs[last_index - 1]

        fibs.append(last + second_last)
        last_index, num = last_index + 1, num - 1

    # the last fibonacci term in our list is the answer
    return fibs[last_index]


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
