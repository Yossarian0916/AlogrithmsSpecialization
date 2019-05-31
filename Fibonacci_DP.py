import timeit


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


def fib_no_memo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib_no_memo(n-1) + fib_no_memo(n-2)


if __name__ == '__main__':
    test_seq = (10, 20, 30)
    for num in test_seq:
        test = timeit.Timer('fib(num, {})', setup='num', globals=globals())
        print(f'fib({num}) cost time:         ', test.timeit(number=100))

    for num in test_seq:
        test = timeit.Timer('fib_no_memo(num)', setup='num', globals=globals())
        print(f'fib_no_memo({num}) cost time: ', test.timeit(number=100))
