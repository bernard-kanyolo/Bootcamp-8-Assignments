import unittest
from fizzbuzz import fizz_buzz


class FizzBuzzTest(unittest.TestCase):
    """Testing the fizzbuzz
    """

    def test_returns_fizz_when_divisible_by_three(self):
        """Test return fizz when input is
        divisible by three
        """
        self.assertEqual(fizz_buzz(3), 'fizz')

    def test_returns_buzz_when_divisible_by_five(self):
        """Test return buzz when input is
        divisible by five
        """
        self.assertEqual(fizz_buzz(5), 'buzz')

if __name__ == '__main__':
    unittest.main()
