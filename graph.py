from collections import defaultdict


class Graph:
    def __init__(self, edges, directed=False):
        self.graph = defaultdict(set)
        self.directed = directed
        self.add_edges(edges)

    def add_edges(self, edges):
        for node1, node2 in edges:
            self.add(node1, node2)

    def add(self, node1, node2):
        self.graph[node1] = node2
        if not self.directed:
            self.graph[node2] = node1

    def remove(self, node):
        for node, neighbors in self.graph.items():
            try:
                neighbors.remove(node)
            except KeyError:
                pass

            try:
                del self.graph[node]
            except KeyError:
                pass

    def find_path(self, start, end, path=[]):
        path = path + [start]
        paths = []
        if start == end:
            return [path]
        else:
            for node in self.graph[start]:
                newpaths = self.find_path(node, end, path)
                if newpaths:
                    for newpath in newpaths:
                        paths.append(newpath)


if __name__ == "__main__":

    graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}
