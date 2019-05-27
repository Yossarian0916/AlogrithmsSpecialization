"""
compute the number of inversions of the given array
running time is O(nlogn)
using divide and conquer
"""


def count_split_inv(array, left, right):
    count = 0
    i = j = 0
    length = len(left) + len(right)
    # sentinal variable
    left.append(float('inf'))
    right.append(float('inf'))

    for k in range(length):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            count += len(left) - 1 - i
            j += 1
    return count


def count_inversion(array):
    """divide and conquer to count the inversion in an array"""
    if len(array) == 1:
        return 0
    else:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        a = count_inversion(left)
        b = count_inversion(right)
        c = count_split_inv(array, left, right)
    return a + b + c


def test_case():
    f = open('IntegerArray.txt', 'r')
    while True:
        try:
            num = int(f.readline().strip('\n'))
            yield num
        except ValueError:
            break
    f.close()


if __name__ == '__main__':
    with open('IntegerArray.txt', 'r') as f:
        inputs = list(map(int, f.read().splitlines()))

    res = count_inversion(inputs)
    print(res)
