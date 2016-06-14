import unittest


def gen_primes(num):
    '''takes a number, n, and returns a list of the first n prime numbers
    if n is less than 1 or not a valid number, it returns the empty list.'''
    try:
        num = int(num)
    except:
        return []

    # empty if we're asked for 0 or less numbers
    if num < 1:
        return []

    # set up the first prime number manually
    primes = [2]
    candidate = 3
    num -= 1

    # decrement num until it's zero while checking every other number (ie. odd
    # numbers) for primality
    while num:
        for prime in primes:
            if candidate % prime == 0:
                break
        else:
            primes.append(candidate)
            num -= 1

        candidate += 2

    return primes


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
