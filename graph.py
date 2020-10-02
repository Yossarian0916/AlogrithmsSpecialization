from collections import defaultdict, deque


class Graph:
    def __init__(self, directed=False, nodes=None, edges=None):
        self.graph = defaultdict(list)
        self.directed = directed
        self.add_nodes(nodes)
        self.add_edges(edges)

    @property
    def nodes(self):
        if not self.directed:
            return list(self.graph.keys())
        elif self.directed:
            nodes = set()
            nodes.update(self.graph.keys())
            for node in self.graph.keys():
                for neighbor in self.graph[node]:
                    nodes.add(neighbor)
            return list(nodes)

    def add_node(self, node):
        if node not in self.nodes:
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

    def bfs(self, v):
        res = list()
        visited = dict.fromkeys(self.nodes, False)
        queue = deque(maxlen=len(self.nodes))
        queue.append(v)
        visited[v] = True
        while queue:
            v = queue.popleft()
            res.append(v)
            for w in self.graph[v]:
                if not visited[w]:
                    queue.append(w)
                    visited[w] = True
        return res

    def dfs(self, v):
        """nonrecursive depth-first-search using stack"""
        visited = dict.fromkeys(self.nodes, False)
        res = list()
        stack = list()
        stack.append(v)
        while stack:
            v = stack.pop()
            if not visited[v]:
                visited[v] = True
                res.append(v)
                for w in self.graph[v]:
                    if not visited[w]:
                        stack.append(w)
        return res

    def dfs_recursive(self, v, visited, res):
        visited[v] = True
        res.append(v)
        for w in self.graph[v]:
            if not visited[w]:
                self.dfs_recursive(w, visited, res)

    def dfs_general(self):
        """depth-first-search on graph, whether connected or not"""
        visited = dict.fromkeys(self.nodes, False)
        res = list()
        for node in self.nodes:
            if not visited[node]:
                self.dfs_recursive(node, visited, res)
        return res

    def topological_util(self, node, visited, label):
        visited[node] = True
        for edge in self.graph[node]:
            if not visited[edge]:
                self.topological_util(edge, visited, label)
        label.appendleft(node)

    def topological_sort(self):
        visited = dict.fromkeys(self.nodes, False)
        # store all nodes in topological order, the index is the position
        label = deque()
        for node in self.nodes:
            if not visited[node]:
                self.topological_util(node, visited, label)
        return label

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
    print("breadth first search: ", graph.bfs(1))
    print("depth first search: ", graph.dfs(1))
    print("recursive depth first search: ", graph.dfs_general())

    diGraph = Graph(True)
    diGraph.add_edges([('a', 'b'), ('a', 'g'), ('b', 'c'),
                       ('g', 'c'), ('c', 'd'), ('c', 'f'),
                       ('d', 'e'), ('d', 'f')])
    print(diGraph.topological_sort())
