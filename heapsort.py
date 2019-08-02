from heap import Heap


def heapsort(array):
    heap = Heap(array)
    heap.build_max_heap()
    for i in range(len(heap.heap)-1, 0, -1):
        # move the maximum to the end of the array
        heap.heap[0], heap.heap[i] = heap.heap[i], heap.heap[0]
        heap.heapsize = heap.heapsize - 1
        heap.max_heapify(0)  # float down the root
    return heap.heap


if __name__ == "__main__":
    lst = [3, 1, 5, 19, 3, 41, 23, 37, 20]
    print(heapsort(lst))
