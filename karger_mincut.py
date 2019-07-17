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
        for line in f.readlines():
            line = list(map(int, line.split('\t')[:-1]))
            for i in range(1, len(line)):
                adj_list[line[0]].append(line[i])

    print(main(adj_list))  # correct answer: 17
