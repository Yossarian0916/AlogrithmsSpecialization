from math import floor


class Heap:
    def __init__(self, array=None):
        self.length = len(array)
        self.heapsize = 0
        self.heap = list(array)

    def __str__(self):
        return str(self.heap)

    __repr__ = __str__

    def __len__(self):
        return self.heapsize

    def parent(self, index):
        return int(floor(index/2))-1

    def left(self, index):
        return 2*(index+1)-1

    def right(self, index):
        return 2*(index+1)

    def max_heapify(self, index):
        left = self.left(index)
        right = self.right(index)
        if left <= self.heapsize-1 and self.heap[left] > self.heap[index]:
            max_id = left
        else:
            max_id = index
        if right <= self.heapsize-1 and self.heap[right] > self.heap[max_id]:
            max_id = right
        if max_id != index:
            self.heap[max_id], self.heap[index] = self.heap[index], self.heap[max_id]
            self.max_heapify(max_id)

    def build_max_heap(self):
        self.heapsize = self.length
        mid_id = int(floor(self.heapsize/2))-1
        for i in range(mid_id, -1, -1):
            self.max_heapify(i)

    def min_heapify(self, index):
        left = self.left(index)
        right = self.right(index)
        if left <= self.heapsize-1 and self.heap[left] < self.heap[index]:
            min_id = left
        else:
            min_id = index
        if right <= self.heapsize-1 and self.heap[right] < self.heap[index]:
            min_id = right
        if min_id != index:
            self.heap[index], self.heap[min_id] = self.heap[min_id], self.heap[index]
            self.min_heapify(min_id)

    def build_min_heap(self):
        self.heapsize = self.length
        mid_id = int(floor(self.heapsize/2))-1
        for i in range(mid_id, -1, -1):
            self.min_heapify(i)

    @staticmethod
    def heapify(array, order):
        heap = Heap(array)
        if order == 'max':
            heap.build_max_heap()
            return heap
        elif order == 'min':
            heap.build_min_heap()
            return heap
        else:
            print('please enter \'max\' or \'min\'')

    def increase_heapsize(self, n):
        self.heapsize = self.heapsize + n

    def decrease_heapsize(self, n):
        self.heapsize = self.heapsize - n


if __name__ == "__main__":
    lst = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    print(Heap.heapify(lst, 'max'))
