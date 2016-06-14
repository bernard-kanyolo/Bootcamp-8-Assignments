def nth_fib(num):
    if num < 1:
        return -1
    elif num == 1:
        return 0
    elif num == 2:
        return 1

    fibs = [0, 1]
    num -= 2
    last_index = len(fibs) - 1

    while num:
        fibs.append(fibs[last_index] + fibs[last_index - 1])
        last_index, num = last_index + 1, num - 1

    return fibs[last_index]
