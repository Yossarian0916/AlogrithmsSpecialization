class Queue:
    def __init__(self, length):
        self.length = length
        self.queue = [None]*(length+1)
        self.head = 0
        self.tail = 0

    def enqueue(self, x):
        if self.is_full():
            return 'Overflow'
        self.queue[self.tail] = x
        if self.tail == self.length:
            self.tail = 0
        else:
            self.tail = self.tail + 1

    def dequeue(self):
        if self.is_empty():
            return 'Underflow'
        x = self.queue[self.head]
        if self.head == self.length:
            self.head = 0
        else:
            self.head = self.head + 1
        return x

    def is_empty(self):
        if self.head == self.tail:
            return True
        return False

    def is_full(self):
        if self.head == self.tail+1 or (self.head == 0 and self.tail == self.length):
            return True
        return False


if __name__ == "__main__":
    queue = Queue(3)
    print(queue.is_empty())
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.queue)
    res = queue.enqueue(4)
    print(res)
    print(queue.queue)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    queue.enqueue(4)
    queue.dequeue()
    queue.enqueue('string')
    print(queue.queue)
    print(queue.is_empty())
