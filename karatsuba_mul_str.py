from math import floor, ceil
import unittest
"""
implement Karatsuba algorithm O(n ** log3)
"""


# karatsuba multiplication
def karatsuba(a, b, base=10):
    """
    divide each number into two halves, the high bits H and the low bits L
    Args:
        a(str): number
        b(str): number
        base: base system, default is base=10
    Return:
        result: int
    """

    # base case
    if len(a) == 1 or len(b) == 1:
        try:
            return int(a) * int(b)
        except ValueError:
            print('Inputs are not valid')
    else:
        # when the inputs have different lengths, padding 0 at the beginning
        if len(a) < len(b):
            a = '0'*(len(b)-len(a)) + a
        elif len(a) > len(b):
            b = '0'*(len(a)-len(b)) + b

        # len of input
        n = max(len(a), len(b))

        # divide number a into high bits and low bits
        aH = a[:n//2]
        aL = a[n//2:]
        # divide number b into high bits and low bits
        bH = b[:n//2]
        bL = b[n//2:]
        # karatsuba multiplication
        aL_bL = karatsuba(aL, bL, base=base)
        aH_bH = karatsuba(aH, bH, base=base)
        aH_aL = str(int(aH) + int(aL))
        bH_bL = str(int(bH) + int(bL))
        aH_bL_aL_bH = karatsuba(aH_aL, bH_bL, base=base) - aH_bH - aL_bL
        # add them together
        result = aH_bH*base**(2*ceil(n/2)) + aH_bL_aL_bH * \
            base**ceil(n/2) + aL_bL
        return result


# define unit test
class TestKaratsuba(unittest.TestCase):

    def test_odd_length(self):
        self.assertEqual(karatsuba('123', '123'), 15129)

    def test_unequal_length(self):
        self.assertEqual(karatsuba('123', '2'), 246)

    def test_input_empty(self):
        with self.assertRaises(TypeError):
            karatsuba('123', '')

    def test_input_not_numeric(self):
        with self.assertRaises(TypeError):
            for i in range(2):
                karatsuba('123', 'dadbsa')
                karatsuba('123', '(*&)-')


if __name__ == '__main__':
    a = '3141592653589793238462643383279502884197169399375105820974944592'
    b = '2718281828459045235360287471352662497757247093699959574966967627'
    ret = karatsuba(a, b, base=10)
    print(f'result: {ret}')

    # unit test begins
    # unittest.main()
