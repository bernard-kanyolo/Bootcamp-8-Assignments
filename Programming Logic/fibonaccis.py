def nth_fib(num):
    '''takes a  number, num, and returns the list fibonacci sequence from 0 to n
    '''

    # validate input
    try:
        num = int(num)
    except:
        return 'invalid input'

    # create fibonacci generator
    def fib_gen():
        '''inner generetor for fib numbers'''
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    # list to hold fib values
    fibs = []

    # create the list
    for fib_num in fib_gen():
        if fib_num <= num:
            fibs.append(fib_num)
        else:
            break

    return fibs
