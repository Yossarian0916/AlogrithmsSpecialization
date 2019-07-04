from collections import defaultdict, deque


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

    def BFS(self, start):
        res = list()
        # mark visited nodes
        visited = dict.fromkeys(self.nodes, False)
        # queue for BFS
        Q = deque(maxlen=len(self.nodes))
        # init
        Q.append(start)
        visited[start] = True
        while Q:
            v = Q.popleft()
            res.append(v)
            for neighbor in self.graph[v]:
                if not visited[neighbor]:
                    Q.append(neighbor)
                    visited[neighbor] = True
        return res

    def DFS(self, start):
        res = list()
        visited = dict.fromkeys(self.nodes, False)
        S = list()
        S.append(start)
        visited[start] = True
        while S:
            v = S.pop()
            res.append(v)
            for neighbor in self.graph[v]:
                if not visited[neighbor]:
                    S.append(neighbor)
                    visited[neighbor] = True
        return res

    def DFS_util(self, start, visited, stack, res):
        stack.append(start)
        visited[start] = True
        while stack:
            v = stack.pop()
            res.append(v)
            for neighbor in self.graph[v]:
                if not visited[neighbor]:
                    self.DFS_util(neighbor, visited, stack, res)

    def DFS_recur(self, start):
        res = list()
        visited = dict.fromkeys(self.nodes, False)
        stack = list()
        self.DFS_util(start, visited, stack, res)
        return res

    def shortest_path_bfs(self, start, end):
        visited = dict.fromkeys(self.nodes, False)
        # keep track of distance
        dist = dict.fromkeys(self.nodes, float('inf'))
        # keep predecessor
        pred = dict.fromkeys(self.nodes, None)

        Q = deque(maxlen=len(self.nodes))
        Q.append(start)
        visited[start] = True
        dist[start] = 0
        while Q:
            v = Q.popleft()
            for neighbor in self.graph[v]:
                if not visited[neighbor]:
                    Q.append(neighbor)
                    pred[neighbor] = v
                    dist[neighbor] = dist[v] + 1
                    visited[neighbor] = True

        if not visited[end]:
            return None
        else:
            distance = dist[end]
            shortest_path = [end]
            while end != start:
                shortest_path.append(pred[end])
                end = pred[end]
            return distance, shortest_path[::-1]


if __name__ == "__main__":
    graph = Graph()
    graph.add_edges([(1, 2), (2, 3), (2, 4), (3, 6),
                     (5, 6), (4, 5), (1, 7), (4, 7)])
    print("depth first search: ", graph.BFS(1))
    print("breadth first search: ", graph.DFS(1))
    print("recursive breadth first search: ", graph.DFS_recur(1))
