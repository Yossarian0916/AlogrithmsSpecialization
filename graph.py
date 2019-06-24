from collections import defaultdict
from queue import Queue


class Graph:
    def __init__(self, directed=False, nodes=None, edges=None):
        self.graph = defaultdict(list)
        self.directed = directed
        self.add_nodes(nodes)
        self.add_edges(edges)

    @property
    def nodes(self):
        return list(self.graph.keys())

    def add_node(self, node):
        self.graph[node] = list()

    def add_nodes(self, nodes):
        if nodes is None:
            return None
        for node in nodes:
            self.add_node(node)

    def remove_node(self, node):
        try:
            del self.graph[node]
        except KeyError:
            print(f'{node} is not in graph')
            return None
        # remove parallel edges, but keep other parallel edges untouched
        for source, adj_list in self.graph.items():
            empty = True
            while empty:
                if node in adj_list:
                    adj_list.remove(node)
                else:
                    empty = False

    def remove_nodes(self, nodes):
        for node in nodes:
            self.remove_node(node)

    @property
    def edges(self):
        edges = list()
        for source, neighbors in self.graph.items():
            for neighbor in neighbors:
                edges.append((source, neighbor))
        return edges

    def add_edge(self, edge):
        node1, node2 = edge
        self.graph[node1].append(node2)
        if not self.directed:
            self.graph[node2].append(node1)

    def add_edges(self, edges):
        if edges is None:
            return None
        for edge in edges:
            self.add_edge(edge)

    def remove_edge(self, edge):
        self.remove_nodes(edge)

    def remove_edges(self, edges):
        for edge in edges:
            self.remove_nodes(edge)

    def bfs(self, start):
        # mark visited nodes
        visited = dict.fromkeys(self.nodes, False)
        # queue for BFS
        Q = Queue(maxsize=len(self.graph))
        # init
        Q.put(start)
        visited[start] = True
        while not Q.empty():
            v = Q.get()
            print(v, end=' ')  # print nodes on screen
            for neighbor in self.graph[v]:
                if not visited[neighbor]:
                    Q.put(neighbor)
                    visited[neighbor] = True


if __name__ == "__main__":
    graph = Graph()
    graph.add_edges([(1, 2), (2, 3), (2, 4), (3, 6),
                     (5, 6), (4, 5), (1, 7), (4, 7)])
    graph.bfs(1)
