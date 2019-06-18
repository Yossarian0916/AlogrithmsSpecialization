from collections import defaultdict
import random


def karger_mincut(graph):
    while len(graph.keys()) > 2:
        u = random.choice(list(graph.keys()))
        v = random.choice(graph[u])
        merge(graph, u, v)

    return len(list(graph.values())[0])


def merge(graph, u, v):
    graph[u] = graph[u] + graph[v]
    while graph[u].count(v) > 0:
        graph[u].remove(v)
    while graph[u].count(u) > 0:
        graph[u].remove(u)
    del graph[v]

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
    graph = defaultdict(list)
    with open("kargerMinCut.txt", "r") as f:
        text = f.read().splitlines()
        for line in text:
            line = list(map(int, line.split('\t')[:-1]))
            for i in range(1, len(line)):
                graph[line[0]].append(line[i])
    print(main(graph))
