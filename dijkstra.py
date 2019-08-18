from collections import defaultdict
from dataclasses import dataclass
from math import floor

from priority_queue import Heapq


class Node:
    def __init__(self, distance, node):
        self.distance = distance
        self.precedessor = node

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            raise NotImplementedError
        else:
            return (self.distance, self.precedessor) == (other.distance, other.precedessor)

    def __str__(self):
        return f'{self.__class__.__name__}(distance={self.distance}, precedessor={self.precedessor})'

    __repr__ = __str__


class DirectedGraph:
    def __init__(self, edges=None):
        self.adj_list = defaultdict(list)
        self.add_weighted_edges(edges)

    @property
    def nodes(self):
        nodes = set()
        nodes.add(self.adj_list.keys())
        for node in self.adj_list.keys():
            for neighbor, weight in self.adj_list[node]:
                nodes.add(neighbor)
        return list(nodes)

    def add_weighted_edges(self, edges):
        if edges is None:
            return None
        for edge in edges:
            self.add_edge(edge)

    def add_weighted_edge(self, edge):
        node1, node2, weight = edge
        self.adj_list[node1].append((node2, weight))

    def dist(self, tail, head):
        for node, weight in self.adj_list[tail]:
            if node == head:
                return weight


def initialize_source(graph, start):
    dist = dict.fromkeys(graph.nodes, float('inf'))
    precedessor = dict.fromkeys(graph.nodes, None)
    dist[start] = 0
    return dist, precedessor


def relax(graph, tail, head):
    if dist[tail] > dist[tail] + graph.dist(tail, head):
        dist[tail] = dist[tail] + graph.dist(tail, head)
        precedessor[head] = tail


def dijkstra(graph, start, end):
    dist, precedessor = initialize_source(graph, start)
    minQ = Heapq(graph.nodes, 'min')
    path = list()
    while not minQ.is_empty():
        u = minQ.extract_min()
        path.append(u)
        for head in graph.adj_list[u]:
            relax(graph, u, head)
    return path


if __name__ == "__main__":
    G = DirectedGraph()
    start = Node(0, None)
    print(start)
