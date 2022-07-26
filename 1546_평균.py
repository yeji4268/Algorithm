N = int(input())
num = list(map(int, input().split()))
max = max(num)
sum = 0
for i in range(N):
    num[i] = num[i] / max * 100
    sum = sum + num[i]
print(sum/N)
