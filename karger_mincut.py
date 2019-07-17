from collections import defaultdict
import random


def karger_mincut(graph, min_v=2):
    while len(graph.keys()) > min_v:
        u = random.choice(list(graph.keys()))
        v = random.choice(graph[u])
        merge(graph, u, v)
    return len(list(graph.values())[0])


def merge(graph, u, v):
    graph[u] = graph[u] + graph[v]
    # merge endpoints, remove end vertex
    del graph[v]
    # replace vertex v with vertex u
    for key, value in graph.items():
        graph[key] = [u if node == v else node for node in graph[key]]
    # remove self-loop
    graph[u] = [node for node in graph[u] if node != u]


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
        for line in f.readlines():
            line = list(map(int, line.split('\t')[:-1]))
            for i in range(1, len(line)):
                graph[line[0]].append(line[i])

    print(main(graph))  # correct answer: 17
