class BinaryHeap:
    def __init__(self, array):
        self.heap = list(array)
        self.length = len(array)  # number of elements in the array
        self.heapsize = 0  # how many elements in the heap are stored here

    def left(self, index):
        """return index of left child node, zero-based indexing"""
        return 2*(index+1)-1

    def right(self, index):
        """return index of right child node, zero-based indexing"""
        return 2*(index+1)

    def parent(self, index):
        """return index of the parent node, zero-based indexing"""
        return int((index-1)/2)

    def is_empty(self):
        return self.heapsize == 0

    def __str__(self):
        return str(self.heap)

    __repr__ = __str__

    def __len__(self):
        return self.heapsize

    def __contains__(self, key):
        if key in self.heap:
            return True
        return False


class MinHeap(BinaryHeap):
    def __init__(self, array):
        super(MinHeap, self).__init__(array)
        self.build_min_heap()

    def min_heapify(self, index):
        left = self.left(index)
        right = self.right(index)
        if left <= self.heapsize-1 and self.heap[left] < self.heap[index]:
            min_id = left
        else:
            min_id = index
        if right <= self.heapsize-1 and self.heap[right] < self.heap[min_id]:
            min_id = right
        if min_id != index:
            self.heap[min_id], self.heap[index] = self.heap[index], self.heap[min_id]
            self.min_heapify(min_id)

    def build_min_heap(self):
        self.heapsize = self.length
        mid_id = int((self.heapsize)/2)-1
        for i in range(mid_id, -1, -1):
            self.min_heapify(i)

    def insert(self, key):
        self.heapsize = self.heapsize + 1
        self.heap.append(float('inf'))
        self.decrease_key(self.heapsize-1, key)

    def delete(self, i):
        if self.heap[i] < self.heap[self.heapsize-1]:
            self.heap[i] = self.heap[self.heapsize-1]
            self.min_heapify(i)
        else:
            self.decrease_key(i, self.heap[self.heapsize-1])
        del self.heap[self.heapsize-1]
        self.heapsize = self.heapsize - 1

    def decrease_key(self, i, key):
        """
        decreases the value of element i's key to the new value key
        for min-priority queue
        """
        if key > self.heap[i]:
            print('new key is greater than current key')
            raise ValueError
        while i > 0 and self.heap[self.parent(i)] > key:
            self.heap[i] = self.heap[self.parent(i)]
            i = self.parent(i)
        self.heap[i] = key

    def minimum(self):
        return self.heap[0]

    def extract_min(self):
        if self.heapsize < 1:
            raise IndexError
        min_key = self.heap[0]
        self.heap[0] = self.heap[self.heapsize-1]
        del self.heap[self.heapsize-1]
        self.heapsize = self.heapsize - 1
        self.min_heapify(0)
        return min_key


class MaxHeap(BinaryHeap):
    def __init__(self, array):
        super(MaxHeap, self).__init__(array)
        self.build_max_heap()

    def insert(self, key):
        self.heapsize = self.heapsize + 1
        self.heap.append(float('-inf'))
        self.increase_key(self.heapsize-1, key)

    def delete(self, i):
        if self.heap[i] > self.heap[self.heapsize-1]:
            self.heap[i] = self.heap[self.heapsize-1]
            self.max_heapify(i)
        else:
            self.increase_key(i, self.heap[self.heapsize-1])
        del self.heap[self.heapsize-1]
        self.heapsize = self.heapsize - 1

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
        mid_id = int((self.heapsize)/2)-1
        for i in range(mid_id, -1, -1):
            self.max_heapify(i)

    def increase_key(self, i, key):
        """
        increases the value of element i's key to the new value key,
        for max-priority queue
        """
        if key < self.heap[i]:
            print('new key is smaller than current key')
            raise ValueError
        while i > 0 and self.heap[self.parent(i)] < key:
            self.heap[i] = self.heap[self.parent(i)]
            i = self.parent(i)
        self.heap[i] = key

    def maximum(self):
        return self.heap[0]

    def extract_max(self):
        if self.heapsize < 1:
            raise IndexError
        max_key = self.heap[0]
        self.heap[0] = self.heap[self.heapsize-1]
        del self.heap[self.heapsize-1]
        self.heapsize = self.heapsize - 1
        self.max_heapify(0)
        return max_key


if __name__ == "__main__":
    array = [10, 5, 2, 6, 3]
    minheap = MinHeap(array)
    print(2 in minheap)
    minheap.insert(15)
    minheap.extract_min()
    print(minheap.heap)
    minheap.extract_min()
    print(minheap.heap)
    print(2 in minheap)
    print(10 in minheap)
