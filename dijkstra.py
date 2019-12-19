from collections import defaultdict


class PriorityQueue:
    """
    each heap element is in form (key value, object handle), while heap
    operations works based on comparing key value and object handle points to
    the corresponding application object.
    """

    def __init__(self, array=[]):
        self._minheap = list(array)
        self._length = len(array)
        self._heapsize = 0
        self._build_min_heap()

    def _left(self, idx):
        return 2*idx+1

    def _right(self, idx):
        return 2*idx+2

    def _parent(self, idx):
        return int((idx-1)/2)

    def _min_heapify(self, idx):
        left = self._left(idx)
        right = self._right(idx)
        min_idx = idx
        if left <= self._heapsize-1 and self._minheap[left] < self._minheap[min_idx]:
            min_idx = left
        if right <= self._heapsize-1 and self._minheap[right] < self._minheap[min_idx]:
            min_idx = right
        if min_idx != idx:
            self._minheap[idx], self._minheap[min_idx] = self._minheap[min_idx], self._minheap[idx]
            self._min_heapify(min_idx)

    def _build_min_heap(self):
        self._heapsize = self._length
        mid_id = int((self._heapsize)/2)-1
        for i in range(mid_id, -1, -1):
            self._min_heapify(i)

    def decrease_key(self, idx, new_key):
        while idx > 0 and new_key < self._minheap[self._parent(idx)]:
            self._minheap[idx] = self._minheap[self._parent(idx)]
            idx = self._parent(idx)
        self._minheap[idx] = new_key

    def extract_min(self):
        if self._heapsize < 1:
            raise IndexError
        minimum = self._minheap[0]
        self._minheap[0] = self._minheap[self._heapsize-1]
        self._heapsize = self._heapsize - 1
        self._min_heapify(0)
        return minimum

    def insert(self, item):
        if item in self._minheap:
            idx = self._minheap.index(item)
            del self._minheap[idx]
            self._heapsize = self._heapsize - 1
        self._minheap.append(item)
        self._heapsize = self._heapsize + 1
        self.decrease_key(self._heapsize-1, item)

    @property
    def minimum(self):
        return self._minheap[0]

    def is_empty(self):
        return self._heapsize == 0

    def __str__(self):
        return str(self._minheap)

    __repr__ = __str__

    def __len__(self):
        return self._heapsize


class DiGraph:
    def __init__(self, edges=None):
        self.adj_list = defaultdict(list)
        self.add_weighted_edges(edges)

    @property
    def nodes(self):
        nodes = set()
        nodes.update(self.adj_list.keys())
        for node in self.adj_list.keys():
            for neighbor, weight in self.adj_list[node]:
                nodes.add(neighbor)
        return list(nodes)

    def add_weighted_edges(self, edges):
        if edges is None:
            return None
        for edge in edges:
            self.add_weighted_edge(edge)

    def add_weighted_edge(self, edge):
        node1, node2, weight = edge
        self.adj_list[node1].append((node2, weight))

    def weight(self, tail, head):
        for node, weight in self.adj_list[tail]:
            if node == head:
                return weight
        return None


def dijkstra(graph, start):
    # initialize
    dist = dict.fromkeys(graph.nodes, float('inf'))
    dist[start] = 0
    min_pq = PriorityQueue()
    min_pq.insert((0, start))
    seen = list()

    while not min_pq.is_empty():
        distance, node = min_pq.extract_min()
        if node in seen:
            continue
        seen.append(node)
        # update distance for not visited nodes
        for neighbor, weight in graph.adj_list[node]:
            if neighbor in seen:
                continue
            if dist[neighbor] > dist[node] + graph.weight(node, neighbor):
                dist[neighbor] = dist[node] + graph.weight(node, neighbor)
                min_pq.insert((dist[neighbor], neighbor))
    return dist


if __name__ == "__main__":
    digraph = DiGraph()
    with open('dijkstraData.txt') as f:
        for line in f.readlines():
            line = line.split()
            node = line[0]
            edges = line[1:]
            for edge in edges:
                neighbor, weight = edge.split(',')
                digraph.add_weighted_edge((node, neighbor, int(weight)))

    res = dijkstra(digraph, '1')
    print(res['7'], res['37'], res['59'], res['82'], res['99'], res['115'],
          res['133'], res['165'], res['188'], res['197'])
    # answer: 2599, 2610, 2947, 2052, 2367, 2399, 2029, 2442, 2505, 3068
