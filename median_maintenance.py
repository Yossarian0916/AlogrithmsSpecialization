"""using my own implementation of priority queue"""
from priorityQ import MaxHeap, MinHeap


def median_in_time(item, heap_low, heap_high):
    """
    find the median in a dynamic way, read the elements one by one, and then
    return the median of the current subarray
    """
    if len(heap_low) == 0:
        heap_low.insert(item)
    else:
        median = heap_low.maximum()
        if item > median:
            heap_high.insert(item)
            if len(heap_high) > len(heap_low):
                tmp = heap_high.extract_min()
                heap_low.insert(tmp)
        else:
            heap_low.insert(item)
            if len(heap_low) - len(heap_high) > 1:
                tmp = heap_low.extract_max()
                heap_high.insert(tmp)
    return heap_low.maximum()


def median_maintenance(array):
    medians = []
    heap_low = MaxHeap([])
    heap_high = MinHeap([])
    for item in array:
        median = median_in_time(item, heap_low, heap_high)
        medians.append(median)
    return medians


if __name__ == "__main__":
    array = []
    with open('Median.txt', 'r') as fd:
        for line in fd:
            array.append(int(line))

    medians = median_maintenance(array)
    print(sum(medians) % 10000)  # 1213
