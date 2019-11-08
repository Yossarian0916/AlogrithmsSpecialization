class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BuildTree:
    def __init__(self, preorder, inorder):
        assert len(preorder) == len(inorder)
        self.preorder = preorder
        self.inorder = inorder
        self.preIdx = 0
        self.root = self.build_tree(0, len(inorder)-1)

    def build_tree(self, inStart, inEnd):
        # terminate condition
        if inStart > inEnd:
            return
        root = Node(key=self.preorder[self.preIdx])
        # pick the next node in preorder traversal as the next root
        self.preIdx += 1
        # if this node has no child
        if inStart == inEnd:
            return root
        # find this node index in inorder traversal
        inIdx = self.inorder.index(root.key)
        # recursive build subtree
        root.left = self.build_tree(inStart, inIdx-1)
        root.right = self.build_tree(inIdx+1, inEnd)
        return root

    def inorder_traversal(self, node, inorder=[]):
        if node is not None:
            inorder = self.inorder_traversal(node.left)
            inorder.append(node.key)
            inorder = self.inorder_traversal(node.right)
        return inorder

    def preorder_traversal(self, node, preorder=[]):
        if node is not None:
            preorder.append(node.key)
            preorder = self.preorder_traversal(node.left)
            preorder = self.preorder_traversal(node.right)
        return preorder

    def traversal(self, order):
        if order == 'inorder':
            print(self.inorder_traversal(self.root))
        elif order == 'preorder':
            print(self.preorder_traversal(self.root))


if __name__ == '__main__':
    preorder = [1, 2, 4, 5, 7, 8, 3, 6]
    inorder = [4, 2, 7, 5, 8, 1, 3, 6]
    tree = BuildTree(preorder, inorder)
    tree.traversal(order='inorder')
    tree.traversal(order='preorder')
