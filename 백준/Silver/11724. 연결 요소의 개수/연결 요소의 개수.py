import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, node, visited):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            dfs(graph, i, visited)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited = [False] * (N + 1)

for i in range(1, N + 1):
    if not visited[i]:
        dfs(graph, i, visited)
        cnt += 1

print(cnt)