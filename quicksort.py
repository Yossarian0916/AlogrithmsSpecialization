import random


def random_partition(array, l, r):
    i = random.randrange(l, r)
    array[l], array[i] = array[i], array[l]
    return partition(array, l, r)


def median_of_three(array, l, r):
    """use median of the left, middle, right elements to be the pivot"""
    mid = (l + r) // 2
    x = array[l] - array[mid]
    y = array[mid] - array[r]
    z = array[r] - array[l]
    if x * y > 0:
        array[mid], array[l] = array[l], array[mid]
    elif y * z > 0:
        array[r], array[l] = array[l], array[r]
    return partition(array, l, r)


def last_element(array, l, r):
    array[l], array[r] = array[r], array[l]
    return partition(array, l, r)


count = 0


def partition(array, l, r):
    global count
    pivot = array[l]  # use the 1st element as pivot
    i = l+1
    for j in range(l+1, r+1):
        if array[j] < pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
    array[l], array[i-1] = array[i-1], array[l]
    count += r-l
    return i-1


def quick_sort(array, l, r):
    if l < r:
        p = random_partition(array, l, r)
        quick_sort(array, l, p-1)
        quick_sort(array, p+1, r)


if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(5000)

    with open('QuickSort.txt', 'r') as f:
        data = f.read().splitlines()
        lst = list(map(int, data))
    # output

    def is_sorted(iter):
        return all(iter[i] <= iter[i+1] for i in range(len(iter)-1))

    quick_sort(lst, 0, len(lst)-1)
    print(is_sorted(lst))
    print(count)
