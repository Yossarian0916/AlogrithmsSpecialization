class Queue:
    def __init__(self, buffersize):
        self.size = buffersize
        self.queue = [None]*buffersize
        self.head = 0
        self.tail = 0

    def enqueue(self, x):
        if (self.head+self.tail) % self.size == 0 and self.tail != 0:
            return 'Overflow'
        self.queue[self.tail % (self.size)] = x
        self.tail = self.tail + 1

    def dequeue(self):
        if self.is_empty():
            return 'Underflow'
        x = self.queue[self.head % (self.size)]
        self.head = self.head + 1
        return x

    def is_empty(self):
        if self.head == self.tail:
            return True
        return False


if __name__ == "__main__":
    queue = Queue(3)
    print(queue.is_empty())
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.is_empty())
