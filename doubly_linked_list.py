class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    """doubly linked list"""

    def __init__(self):
        self.head = None

    def search(self, data):
        node = self.head
        while node is not None and node.data != data:
            node = node.next
        return node

    def __contains__(self, data):
        if self.search(data) is not None:
            return True
        return False

    def insert(self, data):
        """insert data within a new node onto the front of the list"""
        new = Node(data)
        new.next = self.head
        if self.head is not None:
            self.head.prev = new
        self.head = new

    def _delete(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next is not None:
            node.next.prev = node.prev

    def delete(self, data):
        node = self.search(data)
        if self.search(data) is not None:
            self._delete(node)
        else:
            raise ValueError

    def print_list(self):
        pointer = self.head
        while pointer is not None:
            print(pointer.data, '-> ', end='')
            pointer = pointer.next
        print()


if __name__ == "__main__":
    test_ll = LinkedList()
    test_ll.insert(1)
    test_ll.insert(2)
    test_ll.insert(3)
    test_ll.insert('string')
    test_ll.print_list()
    test_ll.delete(3)
    test_ll.print_list()
