class DisjointSet:
    """
    represent disjoint sets by rooted trees, 
    each node with a rank and points to its parent only
    """

    def __init__(self):
        self.root = None
        self.tree = list()
        self.parent = dict()
        self.rank = dict()

    def make_set(self, data):
        self.root = data
        self.tree.append(data)
        self.parent[data] = self.root
        self.rank[data] = 0

    def find(self, x):
        """pass up to find the root and pass back down to update each node to point directly to the root"""
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        return self.link(self.find(x), self.find(y))

    def link(self, x, y):
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
            # if the rank of x, y are the same, also append the tree x to tree y
            # increase the rank of y by 1
            if self.rank[x] == self.rank[y]:
                self.rank[y] = self.rank[y] + 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def count(self):
        return len(self.tree)


if __name__ == '__main__':
    pass
