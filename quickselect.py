import random


def random_selection(array, n):
    if n <= 0 or n > len(array):
        return None
    if len(array) == 1:
        return array[0]
    p = random_partition(array)
    if n-1 == p:
        return array[p]
    elif n-1 < p:
        return random_selection(array[:p], n)
    else:
        return random_selection(array[p:], n-p)


def random_partition(array):
    l = 0
    r = len(array)-1
    p = random.randint(l, r)
    array[p], array[l] = array[l], array[p]
    pivot = array[l]
    i = l + 1
    for j in range(l+1, r+1):
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i-1], array[l] = array[l], array[i-1]
    return i-1
