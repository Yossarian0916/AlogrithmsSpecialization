"""
compute the number of inversions of the given array
running time is O(nlogn)
using divide and conquer
"""

def count_split_inv(left, right):
    count = 0
    length = len(left) + len(right)

    i = j = 0
    for _ in range(length):
        if i >= len(left):
            j += 1
        elif j >= len(right):
            i += 1
        elif left[i] <= right[j]:
            i += 1
        elif left[i] > right[j]:
            j += 1
            count += len(left) - i
    return count


def count_inversion(array):
    """divide and conquer to count the inversion in an array"""
    if len(array) == 1:
        return 0
    else:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        a = b = c = 0
        a = count_inversion(left)
        b = count_inversion(right)
        c = count_split_inv(left, right)

    return a + b + c


if __name__ == '__main__':
    test_lst = [6, 5, 4, 3, 2, 1]
    print(count_inversion(test_lst))