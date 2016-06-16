
def gen_primes(num):
    '''takes a number, num, and returns a list of the first n prime numbers
    if num is less than 1 or not a valid number, it returns the empty list.'''
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
