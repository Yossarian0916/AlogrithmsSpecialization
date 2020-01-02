"""implementation of Prim's algorithm to find a minimum spannning tree"""
from collections import defaultdict
from functools import total_ordering
from typing import Float, List, Dict, Tuple, Any
import random
from BinaryHeap import MinHeap


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


def mst_prim1(graph: Dict[Int, List[Int]], edge_cost: Dict[Tuple[Int, Int], Float]):
    visited_node = set()
    min_spanning_tree = list()
    visited_edge = dict.fromkeys(graph.keys(), False)
    min_heap = MinHeap()
    # init
    start_node = random.choice(list(graph.keys()))
    visited_node.add(start_node)

    while len(visited_node) != len(graph.keys()):
        for node in visited_node:
            for neighbor in graph[node]:
                if (neighbor not in visited_node) and (not visited_edge[(node, neighbor)]):
                    min_heap.insert(edge_cost(node, neighbor))
        weight, edge = min_heap.extract_min()
        visited_node.update([edge[0], edge[1]])
        min_spanning_tree.append(edge)
    return min_spanning_tree


def mst_prim(graph: Dict[Any, List], root: Node, weight: Dict[Tuple, Float]):
    root.key = 0
    Q = MinHeap(graph.nodes)
    while not Q.is_empty():
        u = Q.extract_min()
        for v in graph.adj_list[u]:
            if v in Q and weight[(u, v)] < v.key:
                v.parent = u
                Q.decrease_key(v, v.key, weight[(u, v)])


if __name__ == '__main__':
    pass
