import random


def partition(array, l, r):
    pivot = array[l]  # choose the 1st element as the pivot
    i = l+1
    for j in range(l+1, r):
        if array[j] < pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
    array[l], array[i-1] = array[i-1], array[l]
    return i-1


def random_partition(array, l, r):
    i = random.randrange(l, r)
    array[l], array[i] = array[i], array[l]
    return partition(array, l, r)


def quick_sort(array, l, r):
    if l < r:
        p = random_partition(array, l, r)
        quick_sort(array, l, p)
        quick_sort(array, p+1, r)


if __name__ == "__main__":
    try:
        lst = random.choices(range(1000), k=20)
    except ValueError:
        print('sample size exceeds population size')

    # output
    print('input: ', lst)
    quick_sort(lst, 0, len(lst))
    print('sorted:', lst)
