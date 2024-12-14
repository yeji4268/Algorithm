def deleteNode(num, tree):
    tree[num] = -2
    for i in range(len(tree)):
        if num == tree[i]:
            deleteNode(i, tree)

n = int(input())
tree = list(map(int, input().split()))
d = int(input())
cnt = 0
deleteNode(d, tree)
for i in range(len(tree)):
    if tree[i] != -2 and i not in tree:
        cnt += 1
print(cnt)