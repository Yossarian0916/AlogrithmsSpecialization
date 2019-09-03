from priority_queue import Heapq


def median_in_time(array, idx, median, lower, higher):
    """idx is zero based"""
    new = array[idx]
    if idx == 0:
        median = new

    if new >= median:
        higher.insert(new)
    elif new < median:
        lower.insert(new)

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
