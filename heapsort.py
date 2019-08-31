def max_heapify(heap, idx, heapsize):
    left = 2*idx+1
    right = 2*idx+2
    max_id = idx
    if left <= heapsize-1 and heap[left] > heap[max_id]:
        max_id = left
    if right <= heapsize-1 and heap[right] > heap[max_id]:
        max_id = right
    if max_id != idx:
        heap[idx], heap[max_id] = heap[max_id], heap[idx]
        max_heapify(heap, max_id, heapsize)


def build_max_heap(array):
    mid_id = int(len(array)/2)-1
    for i in range(mid_id, -1, -1):
        max_heapify(array, i, len(array))
    return array


def heapsort(array):
    heap = build_max_heap(array)
    heapsize = len(array)
    for i in range(len(heap)-1, 0, -1):
        # move the maximum to the end of the array
        heap[0], heap[i] = heap[i], heap[0]
        heapsize = heapsize - 1
        max_heapify(heap, 0, heapsize)  # float down the root
    return heap


if __name__ == "__main__":
    lst = [3, 1, 5, 19, 3, 41, 23, 37, 20]
    print(heapsort(lst))
