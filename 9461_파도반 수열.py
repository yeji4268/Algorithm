t = int(input())
num = [1, 1, 1, 2, 2]
for i in range(5, 100):
    num.append(num[i-1]+ num[i-5])
for _ in range(t):
    n = int(input())
    print(num[n-1])
