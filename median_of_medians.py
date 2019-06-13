def Dselect(array, n):
    pivot = choose_pivot(array, len(array))
    p = partition(array, array.index(pivot))
    if p == n-1:
        return array[p]
    elif p < n-1:
        return Dselect(array[p:], n-p)
    else:
        return Dselect(array[:p], n)


def partition(array, p):
    array[0], array[p] = array[p], array[0]
    i = 1
    for j in range(1, len(array)):
        if array[j] < array[0]:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i-1], array[0] = array[0], array[i-1]
    return i-1


def middle(array):
    n = len(array)
    return sorted(array)[n//2]


def choose_pivot(array, n):
    if n < 5:
        median = middle(array)
        return median
    else:
        groups = [array[n:n+5] for n in range(0, n, 5)]
        medians = [middle(group) for group in groups]
        return choose_pivot(medians, len(medians))


if __name__ == "__main__":
    lst = [2, 1, 5, 3, 4, 6, 0, -1]
    print(Dselect(lst, 3))
