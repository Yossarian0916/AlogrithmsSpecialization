class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def search(self, data):
        node = self.head
        while node is not None and node.data != data:
            node = node.next
        return node

    def insert(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def _delete(self, node):
        if self.head == node:
            self.head = node.next
            return

        pointer = self.head
        while pointer is not None and pointer.next != node:
            pointer = pointer.next
        pointer.next = node.next

    def delete(self, data):
        if self.search(data) is not None:
            self._delete(self.search(data))
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
    test_ll.delete('string')
    test_ll.print_list()
