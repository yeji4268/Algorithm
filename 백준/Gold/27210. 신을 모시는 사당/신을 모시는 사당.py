n = int(input())
directions = list(map(int, input().split()))
direction = [0]
sum = 0
for i in range(n):
    if directions[i] == 1:
        sum += 1
    else:
        sum -= 1
    direction.append(sum)
direction.sort()
print(direction[-1] - direction[0])