import sys 
input = sys.stdin.read 
# 재귀 제한 설정 
sys.setrecursionlimit(10**6)

def count_color(x, y, n):
    color = paper[x][y]
    
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != color: # 다른 색이 하나라도 있으면 4등분 
                n_half = n // 2
                w1, b1 = count_color(x, y, n_half)  # 왼쪽 위
                w2, b2 = count_color(x, y + n_half, n_half)  # 오른쪽 위
                w3, b3 = count_color(x + n_half, y, n_half)  # 왼쪽 아래
                w4, b4 = count_color(x + n_half, y + n_half, n_half)  # 오른쪽 아래

                return (w1 + w2 + w3 + w4, b1 + b2 + b3 + b4)
                
    if color == 0:
        return (1, 0)
    else:
        return (0, 1)


data = input().strip().split("\n")
N = int(data[0]) 
paper = [list(map(int, line.split())) for line in data[1:N+1]]


white, blue = count_color(0, 0, N)

print(white)
print(blue)
