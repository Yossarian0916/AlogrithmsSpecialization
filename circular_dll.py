class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class CircularDLL:
    def __init__(self):
        # sentinel
        self.sentinel = Node(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

    def search(self, data):
        node = self.sentinel.next
        while node != self.sentinel and node.data != data:
            node = node.next
        return node

    def insert(self, data):
        """insert new node onto the front of the list"""
        new = Node(data)
        new.next = self.sentinel.next
        self.sentinel.next.prev = new
        self.sentinel.next = new
        new.prev = self.sentinel

    def _delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def delete(self, data):
        node = self.search(data)
        if node is not self.sentinel:
            self._delete(node)
        else:
            raise ValueError

    def print_list(self):
        pointer = self.sentinel.next
        while pointer is not self.sentinel:
            print(pointer.data, '-> ', end='')
            pointer = pointer.next
        # begin a new line
        print()


if __name__ == "__main__":
    circular_dll = CircularDLL()
    circular_dll.insert(1)
    circular_dll.insert(2)
    circular_dll.insert(3)
    circular_dll.insert('string')
    circular_dll.print_list()
    circular_dll.delete(1)
    circular_dll.print_list()
