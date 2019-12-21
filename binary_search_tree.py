class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, data):
        node = self.root
        while node is not None and node.data != data:
            if data > node.data:
                node = node.right
            else:
                node = node.left
        return node

    def insert(self, node):
        trailing_parent = None
        pointer = self.root
        while pointer is not None:
            trailing_parent = pointer
            if node.data > pointer.data:
                pointer = pointer.right
            else:
                pointer = pointer.left
        node.parent = trailing_parent

        if trailing_parent is None:
            self.root = node  # tree was empty
        elif trailing_parent.data < node.data:
            trailing_parent.right = node
        else:
            trailing_parent.left = node

    def transplant(self, replaced, to_plant):
        """
        replaced node's parent becomes to_plant node's parent,
        not attempt to update to_plant.left or to_plant.right,
        it's the resposibility of transplant's caller
        """
        if replaced.parent is None:
            self.root = to_plant
        elif replaced == replaced.parent.left:
            replaced.parent.left = to_plant
        else:
            replaced.parent.right = to_plant
        if to_plant is not None:
            to_plant.parent = replaced.parent

    def delete(self, node):
        if node.left is None:
            self.transplant(node, node.right)
        elif node.right is None:
            self.transplant(node, node.left)
        else:
            succ = self.minimum(node.right)
            if succ.parent != node:
                self.transplant(succ, succ.right)
                succ.right = node.right
                succ.right.parent = succ
            self.transplant(node, succ)
            succ.left = node.left
            succ.left.parent = succ

    def minimum(self, node):
        while node.left is not None:
            node = node.left
        return node

    def maximum(self, node):
        while node.right is not None:
            node = node.right
        return node

    def pred(self, node):
        """find the predecessor of the given key"""
        if node.left is not None:
            return self.maximum(node.left)

        parent = node.parent
        while parent is not None and node == parent.left:
            node = parent
            parent = parent.parent
        return parent

    def succ(self, node):
        """find the successor of the given key"""
        if node.right is not None:
            return self.minimum(node.right)

        parent = node.parent
        while parent is not None and node == parent.right:
            node = parent
            parent = parent.parent
        return parent

    def inorder_recursive(self, node):
        """recursive inorder tree traversal"""
        if node is not None:
            self.inorder_recursive(node.left)
            print(node.data, '-> ', end='')
            self.inorder_recursive(node.right)

    def inorder_iterative(self, node):
        """nonrecursive inorder traversal using one stack"""
        stack = list()
        current = node
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif len(stack) > 0:
                current = stack.pop()
                print(current.data, '-> ', end='')
                current = current.right
            else:
                break

    def morris_inorder_traversal(self, node):
        """
        based on threaded binary tree, make each node as its predecessor's
        right child
        time: O(n), space: O(1)
        """
        while node is not None:
            if node.left is None:
                print(node.key, '-> ', end=' ')
                node = node.right
            else:
                # find the current node's predecessor in its left subtree
                # pre.right != node, it is to prevent from visiting already
                # marked current's predecessor once more
                pre = node.left
                while pre.right is not None and pre.right != node:
                    pre = pre.right
                # make the current node as the right child of its predecessor
                if pre.right is None:
                    pre.right = node
                    node = node.left
                # revert the change made, fix the right child of the predecessor
                else:
                    pre.right = None
                    print(node.key, '-> ', end=' ')
                    node = node.right

    def preorder_recursive(self, node):
        """recursive preorder tree traversal"""
        if node is not None:
            print(node.data, '-> ', end='')
            self.preorder_recursive(node.left)
            self.preorder_recursive(node.right)

    def preorder_iterative(self, node):
        """nonrecursive preorder traversal using one stack"""
        stack = list()
        stack.append(node)
        while len(stack) > 0:
            current = stack.pop()
            print(current.data, '-> ', end='')
            if current.right is not None:
                stack.append(current.right)
            if current.left is not None:
                stack.append(current.left)

    def postorder_recursive(self, node):
        """recursive postorder tree traversal"""
        if node is not None:
            self.postorder_recursive(node.left)
            self.postorder_recursive(node.right)
            print(node.data, '-> ', end='')

    def postorder_iterative(self, node):
        """using two stacks"""
        stack_util = list()
        stack_reverse = list()
        stack_util.append(node)
        while len(stack_util) > 0:
            current = stack_util.pop()
            stack_reverse.append(current)
            if current.left is not None:
                stack_util.append(current.right)
            if current.right is not None:
                stack_util.append(current.right)

        while stack_reverse:
            node = stack_reverse.pop()
            print(node.data, '-> ', end='')

    def postorder_iterative2(self, node):
        """using only one stack"""
        stack = list()
        while True:
            while node is not None:
                if node.right is not None:
                    stack.append(node.right)
                stack.append(node)
                node = node.left
            popped = stack.pop()
            if popped.right == stack[-1]:
                node = stack.pop()
                stack.push(popped)
            else:
                print(popped.data, '-> ', end='')

            if len(stack) <= 0:
                break


if __name__ == "__main__":
    pass
