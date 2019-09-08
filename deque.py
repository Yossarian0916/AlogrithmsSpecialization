class Deque:
    """implement deque using array
    a deque of at most n elements using an array of n+1 element size
    """

    def __init__(self, length):
        self.length = length
        self.deque = [None]*(length+1)
        self.head = 0
        self.tail = 0

    def head_enqueue(self, x):
        if self.is_full():
            return 'Overflow'
        if self.head == 0:
            self.head = self.length
        else:
            self.head = self.head - 1
        self.deque[self.head] = x

    def head_dequeue(self):
        if self.is_empty():
            return 'Underflow'
        x = self.deque[self.head]
        if self.head == self.length:
            self.head = 0
        else:
            self.head = self.head + 1
        return x

    def tail_enqueue(self, x):
        if self.is_full():
            return 'Overflow'
        self.deque[self.tail] = x
        if self.tail == self.length:
            self.tail = 0
        else:
            self.tail = self.tail + 1

    def tail_dequeue(self):
        if self.is_empty():
            return 'Underflow'
        if self.tail == 0:
            self.tail = self.length
        else:
            self.tail = self.tail - 1
        return self.deque[self.tail]

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return self.head == self.tail+1 or (self.head == 0 and self.tail == self.length)


if __name__ == "__main__":
    deque = Deque(3)
    deque.tail_enqueue(2)
    deque.tail_enqueue(3)
    deque.head_enqueue(1)
    print(deque.deque)
    print(deque.head_enqueue('string'))  # output:'Overflow'
    print(deque.head_dequeue())  # output:1
    print(deque.tail_dequeue())  # output:3
    print(deque.head_dequeue())  # output:2
    print(deque.head_dequeue())  # output:'Underflow'
