import unittest
from primes import gen_primes


class GeneratePrimesTestCases(unittest.TestCase):

    def test_lower_edge(self):
        self.assertEqual(gen_primes(0), [],
                         msg='An input of zero should yield an empty list')
        self.assertEqual(gen_primes(-1), [],
                         msg='An input less than 0 should yield an empty list')

    def test_normal_behaviour(self):
        self.assertEqual(gen_primes(1), [2], msg='The first prime number is 2')
        self.assertEqual(gen_primes(2), [2, 3],
                         msg='The first 2 prime numbers are 2 and 3')
        self.assertEqual(gen_primes(10), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],
                         msg='Incorrect list of first 10 prime numbers')

    def test_invalid_input(self):
        self.assertEqual(gen_primes(""), [],
                         msg='A string should return the empty list')
        self.assertEqual(gen_primes({}), [],
                         msg='A dictionary should return the empty list')

if __name__ == '__main__':
    unittest.main()
