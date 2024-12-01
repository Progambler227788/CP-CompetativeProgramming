import heapq
import sys

# Function to perform Dijkstra's algorithm
def dijkstra(n, graph, start):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]  # (distance, node)
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        
        for v, weight in graph[u]:
            new_dist = d + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))
    
    return dist

def find_best_router(n, m, edges):
    # Build the graph as adjacency list
    graph = [[] for _ in range(n + 1)]
    for u, v, d in edges:
        graph[u].append((v, d))
        graph[v].append((u, d))

    min_sum_distance = float('inf')
    best_building = -1
    
    # Calculate the sum of shortest paths for each node
    for i in range(1, n + 1):
        dist = dijkstra(n, graph, i)
        total_distance = sum(dist[1:])  # Sum the distances from i to all other buildings
        
        if total_distance < min_sum_distance:
            min_sum_distance = total_distance
            best_building = i
        elif total_distance == min_sum_distance:
            best_building = min(best_building, i)
    
    return best_building

# Input Reading
t = int(input())  # Number of test cases
for _ in range(t):
    n, m = map(int, input().split())  # Number of buildings and cables
    edges = []
    for _ in range(m):
        u, v, d = input().split()
        u, v, d = int(u), int(v), float(d)
        edges.append((u, v, d))
    
    # Find the building where the router should be placed
    print(find_best_router(n, m, edges))
