"""implementation of bubble sort"""


def bubble_sort(array):
    """sort in incremental order"""
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            print(array)


def short_bubble_sort(array):
    """sort in incremental order, stop early if there is no exchange needed"""
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if not swapped:
            return array

    return array


if __name__ == '__main__':
    lst = [1, 2, 3, 5, 0, 2, 4, 6]
    short_bubble_sort(lst)
    print(lst)
