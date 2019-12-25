from collections import defaultdict
import random


def karger_mincut(input_graph):
    nodes_num = len(input_graph.keys())
    min_cut = float("inf")
    # theoretically, karger_mincut should loop for (n**2)*ln(n)
    for _ in range(nodes_num):
        # each time calculate minimum cut on a shallow copy graph
        graph = input_graph.copy()
        while len(graph.keys()) > 2:
            # pick a random edge from the graph
            u = random.choice(list(graph.keys()))
            v = random.choice(graph[u])
            # merge endpoints, remove end vertex
            graph[u] = graph[u] + graph[v]
            del graph[v]
            # replace vertex v with vertex u
            for key in graph.keys():
                graph[key] = [u if node == v else node for node in graph[key]]
            # remove self-loop
            graph[u] = [node for node in graph[u] if node != u]
        cut_edge_num = len(list(graph.values())[0])
        if cut_edge_num < min_cut:
            min_cut = cut_edge_num
    return min_cut


def random_edge(graph):
    edges = list()
    visited = dict.fromkeys(list(graph.keys()), False)
    for source, neighbors in graph.items():
        for end in neighbors:
            if not visited[end]:
                visited[end] = True
                # for better randomness, change end, source node order
                edges.append((end, source))
    return random.choice(edges)


if __name__ == "__main__":
    graph = defaultdict(list)
    with open("kargerMinCut.txt", "r") as f:
        for line in f.readlines():
            line = list(map(int, line.split('\t')[:-1]))
            for i in range(1, len(line)):
                graph[line[0]].append(line[i])

    print(karger_mincut(graph))  # correct answer: 17
