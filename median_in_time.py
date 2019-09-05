from priority_queue import Heapq


def median_in_time(array, idx, median, lower, higher):
    """
    find the median in a dynamic way, read the elements one by one, and then 
    return the median of the current subarray
    """
    new_item = array[idx]
    if idx == 0:
        median = new_item

    if new_item >= median:
        higher.insert(new_item)
    elif new_item < median:
        lower.insert(new_item)

    length = idx+1
    if length % 2 != 0:
        if len(lower) > len(higher):
            median = lower.maximum()
        elif len(higher) > len(lower):
            median = higher.minimum()
    if length % 2 == 0:
        if len(lower) > len(higher):
            tmp = lower.extract_max()
            higher.insert(tmp)
        elif len(higher) > len(lower):
            tmp = higher.extract_min()
            lower.insert(tmp)
        # lower.maximum, higher.minimum are both the median
        median = lower.maximum()

    return median


if __name__ == "__main__":
    array = [5, 8, 2, 3, 7, 4, 1, 6, 9]
    lower = Heapq([], 'max')
    higher = Heapq([], 'min')
    median = 0
    for i in range(len(array)):
        median = median_in_time(array, i, median, lower, higher)
        print(median)
