from collections import defaultdict
from functools import total_ordering
from typing import Float, List, Dict, Tuple, Any
from BinaryHeap import MinHeap
from union_find import DisjointSet


@total_ordering
class Node:
    def __init__(self, key: Float = float('inf'), parent: Node = None):
        self.key = key
        self.parent = parent

    def __eq__(self, other):
        if type(other) is type(self):
            return self.key == other.key
        return NotImplemented

    def __lt__(self, other):
        if type(other) is type(self):
            return self.key < other.key
        return NotImplemented


class Graph:
    """undirected graph"""

    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_weighted_edges(self, edges: List[Tuple[Node, Node, Float]]):
        for edge in edges:
            self.add_weighted_edge(edge)

    def add_weighted_edge(self, edge: Tuple[Node, Node, Float]):
        source, end, weight = edge
        self.adj_list[source].append((end, weight))
        self.adj_list[end].append((source, weight))

    @property
    def nodes(self) -> List[Node]:
        return list(self.adj_list.keys())

    @property
    def edges(self) -> List[Tuple[Node, Node, Float]]:
        edges = list()
        for key, adjacent in self.adj_list.items:
            for (node, weight) in adjacent:
                edges.append((key, node, weight))
        return edges

    def weight(self, source: Node, end: Node) -> Float:
        for (node, weight) in self.adj_list[source]:
            if node == end:
                return weight
        return None

    def mst_prim(self):
        root.key = self.nodes[0]
        Q = MinHeap(self.nodes)
        while not Q.is_empty():
            u = Q.extract_min()
            for v in self.adj_list[u]:
                if v in Q and self.weight[(u, v)] < v.key:
                    v.parent = u
                    Q.decrease_key(v.key, self.weight[(u, v)])

    def mst_kruskal(self):
        forest = DisjointSet(self.nodes)
        sorted_edges = sorted(self.edges, key=lambda edge: edge[2])
        for edge in sorted_edges:
            if forest.find_set(edge[0]) != forest.find_set(edge[1]):
                edge[0].parent = edge[1]
                forest.union(edge[0], edge[1])

    def print_mst(self):
        mst = list()
        for node in self.nodes:
            mst.append((node, node.parent))
        return mst


if __name__ == '__main__':
    pass
