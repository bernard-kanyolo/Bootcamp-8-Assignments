def fib_to(n):
    '''takes a  number, num, and returns the list fibonacci sequence from 0 to n
    '''

    # validate input
    try:
        n = int(n)
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

    # create the list until our fibonacci numbers >= n
    for index, fib_num in enumerate(fib_gen()):
        if index < n:
            fibs.append(fib_num)
        else:
            break

    return fibs
