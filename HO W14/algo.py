# Topological sort
from collections import deque
def topological_sort(graph):
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = deque([node for node in graph if in_degree[node] == 0])
    sorted_order = []
    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    if len(sorted_order) == len(graph):
        return sorted_order
    else:
        return None
    
graph = {
    'undershorts': ['pants', 'shoes'],
    'pants': ['belt', 'shoes'],
    'belt': ['jacket'],
    'shirt': ['belt', 'tie'],
    'tie': ['jacket'],
    'jacket': [],
    'socks': ['shoes'],
    'shoes': [],
    'watch': []
}

print("\nTopological Sort:")
print(topological_sort(graph))


# Depth-First Search

def dfs(graph, start):
    visited = set()
    stack = [start]
    result = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            stack.extend(reversed(graph[node]))

    return result
   

graph = {
    'u': ['v', 'x'],
    'v': ['y'],
    'y': ['x'],
    'x': ['v'],
    'w': ['y', 'z'],
    'z': ['z']
}

print("\nDepth-First Search:")
print(dfs(graph, 'u'))


# Kruskal algorithm

class DSU:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}
    
    def find(self, item):
        while self.parent[item] != item:
            item = self.parent[item]
        return item
    
    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1

def kruskal(vertices, edges):
    ds = DSU(vertices)
    mst = []
    edges.sort(key=lambda x: x[2])
    cost = 0
    for edge in edges:
        if ds.find(edge[0]) != ds.find(edge[1]):
            ds.union(edge[0], edge[1])
            mst.append(edge)
            cost += edge[2]
    return mst, cost

vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
edges = [
    ('a', 'b', 4),
    ('a', 'h', 8),
    ('b', 'c', 8),
    ('b', 'h', 11),
    ('c', 'd', 7),
    ('c', 'f', 4),
    ('c', 'i', 2),
    ('d', 'e', 9),
    ('d', 'f', 14),
    ('e', 'f', 10),
    ('f', 'g', 2),
    ('g', 'h', 1),
    ('g', 'i', 6),
    ('h', 'i', 7)
]

print("\nKruskal's Algorithm:")
mst, cost = kruskal(vertices, edges)
for edge in mst:
    print(f"{edge[0]} - {edge[1]} (weight: {edge[2]})")
print(f"Total cost: {cost}")