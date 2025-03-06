from collections import deque 

def find_min_time(N, K):
    # 같으면 이동할 필요가 없음
    if N == K:
        return 0 
        
    max_pos = 100000
    visited = [-1] * (max_pos + 1)
    queue = deque([N]) # 시작점 지정 
    visited[N] = 0 
    
    while queue:
        x = queue.popleft() 
        # 이동 가능한 위치 중중
        for p in (x-1, x+1, x*2):
            if (0 <= p and p <= max_pos) and visited[p] == -1: # 범위 내에 있으며, 방문하지 않은 위치 
                visited[p] = visited[x] + 1 
                queue.append(p)
                
                if p == K: 
                    return visited[p]

N, K = map(int, input().split())
print(find_min_time(N, K))