import sys
from collections import deque

def find_parents_bfs(n, edges):
    graph = [[] for _ in range(n + 1)]
    
    # 무방향 그래프 
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    parents = [0] * (n + 1)
    
    # BFS
    queue = deque([1])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]: 
            if parents[neighbor] == 0: 
                parents[neighbor] = node 
                queue.append(neighbor)
    
    # 부모 노드 출력 
    for i in range(2, n + 1):
        print(parents[i])

n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

find_parents_bfs(n, edges)
