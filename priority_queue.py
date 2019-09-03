class Heapq:
    def __init__(self, array, order):
        self.heapq = list(array)
        self.length = len(array)  # number of elements in the array
        self.heapsize = 0  # how many elements in the heap are stored here
        self.order = order  # 'max' or 'min'
        if self.order == 'max':
            self.build_max_heap()
        elif self.order == 'min':
            self.build_min_heap()
        else:
            raise ValueError

    def __str__(self):
        return str(self.heapq)

    __repr__ = __str__

    def __len__(self):
        return self.heapsize

    @staticmethod
    def heapify(array, order):
        heapq = Heapq(array, order)
        return heapq

    def is_empty(self):
        return self.heapsize == 0

    def left(self, index):
        """return index of left child node, zero-based indexing"""
        return 2*(index+1)-1

    def right(self, index):
        """return index of right child node, zero-based indexing"""
        return 2*(index+1)

    def parent(self, index):
        """return index of the parent node, zero-based indexing"""
        return int((index-1)/2)

    def max_heapify(self, index):
        left = self.left(index)
        right = self.right(index)
        if left <= self.heapsize-1 and self.heapq[left] > self.heapq[index]:
            max_id = left
        else:
            max_id = index
        if right <= self.heapsize-1 and self.heapq[right] > self.heapq[index]:
            max_id = right

        if max_id != index:
            self.heapq[max_id], self.heapq[index] = self.heapq[index], self.heapq[max_id]
            self.max_heapify(max_id)

    def build_max_heap(self):
        self.heapsize = self.length
        mid_id = int((self.heapsize)/2)-1
        for i in range(mid_id, -1, -1):
            self.max_heapify(i)

    def min_heapify(self, index):
        left = self.left(index)
        right = self.right(index)
        if left <= self.heapsize-1 and self.heapq[left] < self.heapq[index]:
            min_id = left
        else:
            min_id = index
        if right <= self.heapsize-1 and self.heapq[right] < self.heapq[index]:
            min_id = right

        if min_id != index:
            self.heapq[min_id], self.heapq[index] = self.heapq[index], self.heapq[min_id]
            self.min_heapify(min_id)

    def build_min_heap(self):
        self.heapsize = self.length
        mid_id = int((self.heapsize)/2)-1
        for i in range(mid_id, -1, -1):
            self.min_heapify(i)

    def insert(self, key):
        self.heapsize = self.heapsize + 1
        if self.order == 'max':
            self.heapq.append(float('-inf'))
            self.increase_key(self.heapsize-1, key)
        elif self.order == 'min':
            self.heapq.append(float('inf'))
            self.decrease_key(self.heapsize-1, key)

    def delete(self, i):
        if self.order == 'max':
            if self.heapq[i] > self.heapq[self.heapsize-1]:
                self.heapq[i] = self.heapq[self.heapsize-1]
                self.max_heapify(i)
            else:
                self.increase_key(i, self.heapq[self.heapsize-1])
        elif self.order == 'min':
            if self.heapq[i] < self.heapq[self.heapsize-1]:
                self.heapq[i] = self.heapq[self.heapsize-1]
                self.min_heapify(i)
            else:
                self.decrease_key(i, self.heapq[self.heapsize-1])
        # del self.heapq[self.heapsize-1]
        self.heapsize = self.heapsize - 1

    def increase_key(self, i, key):
        """
        increases the value of element i's key to the new value key,
        for max-priority queue
        """
        if key < self.heapq[i]:
            print('new key is smaller than current key')
            raise ValueError
        while i > 0 and self.heapq[self.parent(i)] < key:
            self.heapq[i] = self.heapq[self.parent(i)]
            i = self.parent(i)
        self.heapq[i] = key

    def decrease_key(self, i, key):
        """
        decreases the value of element i's key to the new value key
        for min-priority queue
        """
        if key > self.heapq[i]:
            print('new key is greater than current key')
            raise ValueError
        while i > 0 and self.heapq[self.parent(i)] > key:
            self.heapq[i] = self.heapq[self.parent(i)]
            i = self.parent(i)
        self.heapq[i] = key

    def maximum(self):
        if self.order == 'max':
            return self.heapq[0]
        else:
            print('this is not a max-priority queue')

    def minimum(self):
        if self.order == 'min':
            return self.heapq[0]
        else:
            print('this is not a min-priority queue')

    def extract_max(self):
        if self.heapsize < 1:
            raise IndexError
        max_key = self.heapq[0]
        self.heapq[0] = self.heapq[self.heapsize-1]
        self.heapsize = self.heapsize - 1
        self.max_heapify(0)
        return max_key

    def extract_min(self):
        if self.heapsize < 1:
            raise IndexError
        min_key = self.heapq[0]
        self.heapq[0] = self.heapq[self.heapsize-1]
        self.heapsize = self.heapsize - 1
        self.min_heapify(0)
        return min_key


if __name__ == "__main__":
    pass
