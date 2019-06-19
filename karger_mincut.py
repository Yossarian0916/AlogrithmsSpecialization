from collections import defaultdict
import random


class Graph:
    def __init__(self, adj_list):
        self.graph = adj_list

    @property
    def nodes(self):
        nodes = list()
        for node in self.graph.keys():
            nodes.append({node})
        return nodes

    @property
    def edges(self):
        edges = list()
        for start, endpoints in self.graph.items():
            for endpoint in endpoints:
                edges.append((start, endpoint))
        return edges


def karger_mincut(graph):
    while len(graph.keys()) > 2:
        u = random.choice(list(graph.keys()))
        v = random.choice(graph[u])
        merge(graph, u, v)

    return len(list(graph.values())[0])


def merge(graph, u, v):
    graph[u] = graph[u] + graph[v]
    # remove self-loop
    while graph[u].count(v) > 0:
        graph[u].remove(v)
    while graph[u].count(u) > 0:
        graph[u].remove(u)
    # merge endpoints, remove end vertex
    del graph[v]

    # replace vertex v with vertex u
    for start in graph.keys():
        for idx, end in enumerate(graph[start]):
            if end == v:
                graph[start][idx] = u


def main(graph, minimum=None):
    for _ in range(200**3):
        try:
            if karger_mincut(graph) < minimum:
                minimum = karger_mincut(graph)
        except TypeError:
            minimum = karger_mincut(graph)
    return minimum


if __name__ == "__main__":
    adj_list = defaultdict(list)
    with open("kargerMinCut.txt", "r") as f:
        text = f.read().splitlines()
        for line in text:
            line = list(map(int, line.split('\t')[:-1]))
            for i in range(1, len(line)):
                adj_list[line[0]].append(line[i])

    test = Graph(adj_list)
