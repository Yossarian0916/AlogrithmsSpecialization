import timeit


def fib_no_memo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib_no_memo(n-1) + fib_no_memo(n-2)


def fib(n, cache=None):
    try:
        return cache[n]
    except KeyError:
        if n == 0 or n == 1:
            cache[n] = 1
            return 1
        else:
            res = fib(n-1, cache) + fib(n-2, cache)
            cache[n] = res
            return res


cache = dict()
def fib_dp(n):
    try:
        return cache[n]
    except KeyError:
        if n == 0 or n == 1:
            cache[n] = 1
            return 1
        else:
            res = fib_dp(n-1) + fib_dp(n-2)
            cache[n] = res
            return res


def fib_back(n):
    a = b = 1
    for i in range(2, n+1):
        a, b = b, a+b
    return b


if __name__ == '__main__':
    test_seq = (10, 20, 30)
    for num in test_seq:
        test = timeit.Timer('fib(num, {})', setup='num', globals=globals())
        print(f'fib({num}) cost time:         ', test.timeit(number=100))
    print()

    for num in test_seq:
        test = timeit.Timer('fib_dp(num)', setup='num', globals=globals())
        print(f'fib_dp({num}) cost time:      ', test.timeit(number=100))
    print()

    for num in test_seq:
        test = timeit.Timer('fib_back(num)', setup='num', globals=globals())
        print(f'fib_back({num}) cost time:    ', test.timeit(number=100))
    print()

    for num in test_seq:
        test = timeit.Timer('fib_no_memo(num)', setup='num', globals=globals())
        print(f'fib_no_memo({num}) cost time: ', test.timeit(number=100))
