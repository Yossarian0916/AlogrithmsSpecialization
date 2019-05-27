def karatsuba(x, y, base=10):
    """
    Karatsuba Mulitiplication, complexity O(n**log3)
    Args:
        x, y(int): default base is 10
        base: default=10
    """
    if len(str(x)) or len(str(y)) == 1:
        try:
            return x * y
        except ValueError:
            print('inputs are not valid!')
    else:
        length = max(len(str(x)), len(str(y)))
        m = length // 2

        # divide inputs into two halves
        a = x // base**m
        b = x % base**m
        c = y // base**m
        d = y % base**m

        ac = karatsuba(a, c, base=base)
        bd = karatsuba(b, d, base=base)
        ad_plus_bc = karatsuba(a+b, c+d, base=base) - ac - bd
        # add them together
        result = ac*base**(2*m) + ad_plus_bc*base**m + bd
        return result


if __name__ == '__main__':

    a = 3141592653589793238462643383279502884197169399375105820974944592
    b = 2718281828459045235360287471352662497757247093699959574966967627
    ret = karatsuba(a, b)
    print(ret)
