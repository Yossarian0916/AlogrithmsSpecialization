import heapq


def median_in_time(item, heap_low=[], heap_high=[]):
    """
    find the median in a dynamic way, read the elements one by one, and then
    return the median of the current subarray
    """
    if len(heap_low) == 0:
        heapq.heappush(heap_low, -item)
    else:
        median = -heap_low[0]
        if item > median:
            heapq.heappush(heap_high, item)
            if len(heap_high) > len(heap_low):
                tmp = heapq.heappop(heap_high)
                heapq.heappush(heap_low, -tmp)
        else:
            heapq.heappush(heap_low, -item)
            if len(heap_low) - len(heap_high) > 1:
                tmp = heapq.heappop(heap_low)
                heapq.heappush(heap_high, -tmp)
    return -heap_low[0]


def median_maintenance(array):
    medians = []
    for item in array:
        median = median_in_time(item)
        medians.append(median)
    return medians


if __name__ == "__main__":
    array = []
    with open('Median.txt', 'r') as fd:
        for line in fd:
            array.append(int(line))

    medians = median_maintenance(array)
    print(sum(medians) % 10000)  # 1213
