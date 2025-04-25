# Dijkstra's Algorithm 

import heapq
def dijkstra(graph, start):
    queue = [(0, start)]
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances


# Bellman-Ford Algorithm
def bellman_ford(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("Graph contains a negative-weight cycle")

    return distances


# Floyd-Warshall Algorithm

def floyd_warshall(graph):
    nodes = list(graph.keys())
    distances = {node: {n: float('infinity') for n in nodes} for node in nodes}
    for node in nodes:
        distances[node][node] = 0

    for node in graph:
        for neighbor, weight in graph[node].items():
            distances[node][neighbor] = weight
    
    for k in nodes:
        for i in nodes:
            for j in nodes:
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
    
    result = {node: distances[node] for node in nodes}
    return result


if __name__ == "__main__":
    graph = {
        'A': {'B': 10, 'C': 3},
        'B': {'C': 1, 'D': 2},
        'C': {'B': 4, 'D': 8, 'E': 2},
        'D': {'E': 7},
        'E': {'D': 9}
    }

    negative_weight_graph = {
        'A': {'B': -1, 'C': 4},
        'B': {'C': 3, 'D': 2, 'E': 2},
        'C': {},
        'D': {'B': 1, 'C': 5},
        'E': {'D': -3}
    }

    print("Dijkstra's Algorithm:", dijkstra(graph, 'A'))
    print("\nBellman-Ford Algorithm:", bellman_ford(graph, 'A'))
    print("\nBellman-Ford Algorithm with negative weights:", bellman_ford(negative_weight_graph, 'A'))
    print("\nFloyd-Warshall Algorithm:", floyd_warshall(graph)) 
    print("\nFloyd-Warshall Algorithm with negative weights:", floyd_warshall(negative_weight_graph))