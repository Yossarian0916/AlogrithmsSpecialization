RED = 'red'
BLACK = 'black'


class Node:
    def __init__(self, data, color):
        self.data = data
        self.color = color
        self.parent = None
        self.left = None
        self.right = None

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return NotImplemented


class RedBlackTree:
    def __init__(self):
        self.sentinel = Node(None, BLACK)
        self.root = self.sentinel

    def search(self, node):
        raise NotImplementedError

    def left_rotation(self, node):
        """assumption: node.right is not None"""
        # set y points to node.right
        y = node.right
        # turn y's left subtree into x's right subtree
        node.right = y.left
        if y.left != self.sentinel:
            y.left.parent = node
        # link node's parent to y
        y.parent = node.parent
        if node.parent == self.sentinel:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        # put node on y's left
        y.left = node
        node.parent = y

    def right_rotation(self, node):
        """assumption: node.right is not None"""
        # set x points to node.left
        x = node.left
        # turn x's right subtree to x's left subtree
        node.left = x.right
        if x.right != self.sentinel:
            x.right.parent = node
        # link node's parent to x
        x.parent = node.parent
        if node.parent == self.sentinel:
            self.root = x
        elif node == node.parent.left:
            node.parent.left = x
        else:
            node.parent.right = x
        # turn node into x's right child
        x.right = node
        node.parent = x

    def rb_insert(self, node):
        trailing = self.sentinel
        pointer = self.root
        while pointer != self.sentinel:
            trailing = pointer
            if node.data < pointer.data:
                pointer = pointer.left
            else:
                pointer = pointer.right
        node.parent = trailing
        if trailing == self.sentinel:
            self.root = node
        elif node.data < trailing.data:
            trailing.left = node
        else:
            trailing.right = node
        node.left = self.sentinel
        node.right = self.sentinel
        node.color = RED  # color new inserted node as red
        self.rb_insert_fixup(node)

    def rb_insert_fixup(self, node):
        while node.parent.color == RED:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotation(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.right_rotation(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotation(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.left_rotation(node.parent.parent)
        self.root.color = BLACK

    def minimum(self, node):
        while node.left != self.sentinel:
            node = node.left
        return node

    def maximum(self, node):
        while node.right != self.sentinel:
            node = node.right
        return node

    def rb_transplant(self, removed, to_plant):
        if removed.parent == self.sentinel:
            self.root = to_plant
        elif removed == removed.parent.left:
            removed.parent.left = to_plant
        else:
            removed.parent.right = to_plant
        to_plant.parent = removed.parent

    def rb_delete(self, node):
        """
        y is the node to be removed or the node that is moved within the tree
        x points to the node that moves into y's original position
        """
        y = node
        y_original_color = y.color
        if node.left == self.sentinel:
            x = node.right
            self.rb_transplant(node, node.right)
        elif node.right == self.sentinel:
            x = node.left
            self.rb_transplant(node, node.left)
        else:
            y = self.minimum(node.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node:
                # setting x.p to y, even if x == self.sentinel
                x.parent = y
            else:
                self.rb_transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.rb_transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color
        if y_original_color == BLACK:
            self.rb_delete_fixup(x)

    def rb_delete_fixup(self, x):
        """
        because we remove the black node y from its original position,
        now assume that y passes its blackness to its position inheritor node x,
        so x is now either 'red-and-black' or 'doubly black'.
        re_delete_fixup is to remove this extra blackness on the node x

        w is the x's sibling
        """
        while x != self.root and x.color == BLACK:
            # x is a left child
            if x == x.p.left:
                w = x.p.right
                # case 1
                # case 1 will be converted to case 2, 3 or 4
                if w.color == RED:
                    w.color = BLACK
                    x.p.color = RED
                    self.left_roatation(x.p)
                    w = x.p.right
                # case 2
                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED
                    x = x.p
                # case 3: w.right is black, w.left is red
                # case 3 will be converted into case 4
                else:
                    if w.right.color == BLACK:
                        w.left.color = BLACK
                        w.color = RED
                        self.right_rotation(w)
                        w = x.p.right
                # case 4: w.right is red, w.left.color doesn't matter
                    w.color = x.p.color
                    x.p.color = BLACK
                    w.right.color = BLACK
                    self.left_rotation(x.p)
                    x = self.root

            # x is a right child
            else:
                w = x.p.left
                # case 5, symmetry to case 1
                if w.color == RED:
                    w.color = BLACK
                    x.p.color = RED
                    self.right_rotation(x.p)
                    w = x.p.left
                # case 6, symmetry to case 2
                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED
                    x = x.p
                # case 7, symmetry to case 3
                else:
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self.left_rotation(w)
                        w = x.p.left
                # case 8, symmetry to case 4
                    w.color = x.p.color
                    x.p.color = BLACK
                    w.left.color = BLACK
                    self.right_rotation(x.p)
                    x = self.root
        x.color = BLACK

    def pred(self, node):
        raise NotImplementedError

    def succ(self, node):
        raise NotImplementedError
