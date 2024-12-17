N = int(input())
P = sorted(list(map(int, input().split())))
tot = 0

for i in range(1, N+1):
    tot += sum(P[:i])
print(tot)