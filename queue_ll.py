class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    __repr__ = __str__


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        if self.tail is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            res = self.head
            self.head = self.head.next
            return str(res)

    def is_empty(self):
        return self.head is None


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.is_empty())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.is_empty())
    print(queue.dequeue())
