from collections import defaultdict
import sys
import threading

sys.setrecursionlimit(8000000)
threading.stack_size(67108864)


class Graph:
    def __init__(self, directed=True, edges=None):
        self.graph = defaultdict(list)
        self.directed = True
        self.add_edges(edges)

    @property
    def nodes(self):
        if not self.directed:
            return list(self.graph)
        else:
            nodes = set()
            nodes.update(self.graph.keys())
            for node in self.graph.keys():
                for neighbor in self.graph[node]:
                    nodes.add(neighbor)
            return list(nodes)

    def add_edge(self, edge):
        node1, node2 = edge
        self.graph[node1].append(node2)
        if not self.directed:
            self.graph[node2].append(node1)

    def add_edges(self, edges):
        if edges is None:
            return None
        else:
            for edge in edges:
                self.add_edge(edge)

    def reverse(self):
        """reverse all arcs in the directed graph"""
        if not self.directed:
            return self.graph
        else:
            reversed_graph = Graph(True, None)
            for tail in self.nodes:
                for head in self.graph[tail]:
                    reversed_graph.add_edge((head, tail))
            return reversed_graph

    def finish_order(self, s, visited, finished):
        visited[s] = True
        for v in self.graph[s]:
            if not visited[v]:
                visited[v] = True
                self.finish_order(v, visited, finished)
        finished.append(s)

    def DFS_util(self, s, visited, leader, scc):
        visited[s] = True
        # scc[leader].append(s)
        scc[leader] += 1
        for v in self.graph[s]:
            if not visited[v]:
                visited[v] = True
                self.DFS_util(v, visited, leader, scc)

    def kosaraju(self):
        """use two DFS to find strongly connected components"""
        visited = dict.fromkeys(self.nodes, False)
        finished = list()
        scc = defaultdict(int)
        # 1st DFS pass, compute each node finishing time
        graph_transposed = self.reverse()
        for node in self.nodes:
            if not visited[node]:
                graph_transposed.finish_order(node, visited, finished)
        # 2nd DFS pass, compute scc
        visited = dict.fromkeys(visited, False)
        for node in reversed(finished):
            if not visited[node]:
                leader = node
                self.DFS_util(node, visited, leader, scc)

        return scc


if __name__ == "__main__":
    # G = Graph(edges=[('a', 'b'), ('b', 'c'), ('c', 'a'), ('b', 'e'), ('e', 'f'),
    #                  ('f', 'g'), ('g', 'e'), ('f', 'h'), ('h', 'i'), ('i', 'j'),
    #                  ('j', 'h')])
    # print(G.kosaraju())

    def main():
        G = Graph()
        with open("SCC.txt", "r") as f:
            for edge in f.readlines():
                G.add_edge(edge.split())
        res = G.kosaraju()
        print(sorted(res.values(), reverse=True)[:5])

    thread = threading.Thread(target=main)
    thread.setDaemon(True)
    thread.start()
    thread.join()  # wait till kosaraju thread finishes
    print("END")  # back to the main thread
