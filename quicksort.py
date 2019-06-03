import random
import timeit

count = 0


def partition(array, l, r):
    global count
    pivot = array[l]  # use the 1st element as pivot
    i = l+1
    for j in range(l+1, r):
        if array[j] < pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
    array[l], array[i-1] = array[i-1], array[l]
    count += r-l-1
    return i-1


def random_partition(array, l, r):
    i = random.randrange(l, r)
    array[l], array[i] = array[i], array[l]
    return partition(array, l, r)


def median_of_three(array, l, r):
    mid = (l + r-1) // 2
    # only use median element as pivot
    # x = array[l] - array[mid]
    # y = array[mid] - array[r-1]
    # z = array[r-1] - array[l]
    # if x * y > 0:
    #     array[mid], array[l] = array[l], array[mid]
    # elif y * z > 0:
    #     array[r-1], array[l] = array[l], array[r-1]
    # return partition(array, l, r)
    # use median element as pivot, and sort these three elements
    if array[l] < array[mid]:
        array[l], array[mid] = array[mid], array[l]
    if array[r-1] < array[mid]:
        array[r-1], array[mid] = array[mid], array[r-1]
    if array[r-1] < array[l]:
        array[r-1], array[l] = array[l], array[r-1]
    return partition(array, l, r)


def last_element(array, l, r):
    array[l], array[r-1] = array[r-1], array[l]
    return partition(array, l, r)


def quick_sort(array, l, r):
    if l < r:
        p = median_of_three(array, l, r)
        quick_sort(array, l, p)
        quick_sort(array, p+1, r)


if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(5000)

    with open('QuickSort.txt', 'r') as f:
        data = f.read().splitlines()
        lst = list(map(int, data))
    # output
    quick_sort(lst, 0, len(lst))
    print(count)
