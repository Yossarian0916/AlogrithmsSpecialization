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
            # len(left) counts the additional sentinal 'inf'
            count += len(left) - i - 1
            j += 1
    return count


def count_inversion(array):
    """divide and conquer to count the inversion in an array"""
    if len(array) == 1:
        return 0

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    a = count_inversion(left)
    b = count_inversion(right)
    c = count_split_inv(array, left, right)
    return a + b + c


def read_input():
    with open('IntegerArray.txt', 'r') as f:
        while True:
            try:
                num = int(f.readline().strip('\n'))
                yield num
            except ValueError:
                break


if __name__ == '__main__':
    with open('IntegerArray.txt', 'r') as f:
        inputs = list()
        for line in f.readlines():
            inputs.append(int(line))

    print(len(inputs))
    res = count_inversion(inputs)
    print(res)  # 2407905288
