class DisjointSet:
    """
    represent disjoint sets by rooted trees,
    each node with a rank and points to its parent only
    """

    def __init__(self, array):
        self.make_set(array)
        self.count = len(array)  # size of disjoint components

    def make_set(self, array):
        self.parent = {item: item for item in array}
        self.rank = dict.fromkeys(array, 0)

    def find_set(self, x):
        """
        path compression:
        pass up to find the root
        and pass back down to update each node to point directly to the root
        """
        if x != self.parent[x]:
            self.parent[x] = self.find_set(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        if self.connected(x, y):
            return
        # each union, the num of differents sets reduce self by 1
        self.count = self.count - 1
        self.link(self.find_set(x), self.find_set(y))

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
        return (self.find_set(x) == self.find_set(y))

    def count(self):
        return self.count
