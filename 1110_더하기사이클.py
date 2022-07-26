N = int(input())
cnt = 0
origin = N

while True:
    a = N // 10  
    b = N % 10
    c = (a + b) // 10
    d = (a + b) % 10
    N = b * 10 + d
    cnt = cnt + 1
    
    if N == origin :
        break
print(cnt)
