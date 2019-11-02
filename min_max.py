"""3*floor(n/2) to find minimum and maximum at the same time"""


def min_max(array):
    # init min, max
    if len(array) % 2 == 0:
        min = array[0] < array[1] and array[0] or array[1]
        max = array[0] > array[1] and array[0] or array[1]
    elif len(array) % 2 != 0:
        min = max = array[0]
    return compare_pairs(array, 2)


def compare_pairs(array, start):
    """
    compare each pair of elements first with each other, and then compare the 
    smaller with the current minimum and the larger to the current maximum.
    at a cost of 3 comparison for every 2 elements
    """
    for i in range(start, len(array), 2):
        if array[i] < array[i+1]:
            min_temp, max_temp = array[i], array[i+1]
        else:
            min_temp, max_temp = array[i+1], array[i]
        if min > min_temp:
            min = min_temp
        if max < max_temp:
            max = max_temp
    return min, max
