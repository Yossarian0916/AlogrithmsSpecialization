import timeit


def fib_recursion(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib_recursion(n-1) + fib_recursion(n-2)


def fib_dp(n, cache=None):
    try:
        return cache[n]
    except KeyError:
        if n == 0 or n == 1:
            cache[n] = 1
            return 1
        else:
            res = fib_dp(n-1, cache) + fib_dp(n-2, cache)
            cache[n] = res
            return res


buffer = dict()


def fib_dp_LBYL(n):
    if n == 0 or n == 1:
        return 1
    if n in buffer:
        return buffer[n]
    else:
        res = fib_dp_LBYL(n-2) + fib_dp_LBYL(n-2)
        buffer[n] = res
        return res


cache = dict()


def fib_dp_EAFP(n):
    try:
        return cache[n]
    except KeyError:
        if n == 0 or n == 1:
            cache[n] = 1
            return 1
        else:
            res = fib_dp_EAFP(n-1) + fib_dp_EAFP(n-2)
            cache[n] = res
            return res


def fib_bottom_up(n):
    a = b = 1
    for _ in range(2, n+1):
        a, b = b, a+b
    return b


if __name__ == '__main__':
    test_seq = (10, 100, 1000)

    for num in test_seq:
        test = timeit.Timer('fib_dp_LBYL(num)', setup='num', globals=globals())
        print(f'fib_dp_LBYL({num}) cost time:  ', test.timeit(number=100000))
    print()

    for num in test_seq:
        test = timeit.Timer('fib_dp_EAFP(num)', setup='num', globals=globals())
        print(f'fib_dp_EAFP({num}) cost time:  ', test.timeit(number=100000))
    print()

    for num in test_seq:
        test = timeit.Timer('fib_bottom_up(num)',
                            setup='num', globals=globals())
        print(f'fib_bottom_up({num}) cost time:', test.timeit(number=100000))
