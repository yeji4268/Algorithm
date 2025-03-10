from collections import deque 

def BFS(n, m, grid, start):
    dis = [[-1] * m for _ in range(n)]
    queue = deque([start])
    
    sx, sy = start 
    dis[sx][sy] = 0
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy 
            # 범위 내에 있고, 방문하기 전이며, 갈 수 있는 땅(1)인 경우 
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and dis[nx][ny] == -1:
                dis[nx][ny] = dis[x][y] + 1 
                queue.append((nx, ny))
                
    # 갈 수 없는 땅(0)
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                dis[i][j] = 0 
    return dis 

n, m = map(int, input().split())
grid = [] 
start = None 

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 2:
            start = (i, j)
    grid.append(row)

result = BFS(n, m, grid, start)

for row in result:
    print(" ".join(map(str, row)))