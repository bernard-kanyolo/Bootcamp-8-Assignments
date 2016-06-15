def fizz_buzz(number):
    """return fizz when divisible by 3
    return buzz when divisible by 5
    return fizzbuzz when divisible by both 3 and 5
    """
    if number % 3 == 0 and number % 5 == 0:
        return "fizzbuzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
