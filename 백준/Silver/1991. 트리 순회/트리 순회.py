tree = dict()

# preorder: 루트 -> 왼쪽 -> 오른쪽 
def preorder(node):
    if node:
        print(node, end = "")
        preorder(tree[node][0]) 
        preorder(tree[node][1])

# inorder: 왼쪽 -> 루트 -> 오른쪽 
def inorder(node):
    if node:
        inorder(tree[node][0])
        print(node, end = "")
        inorder(tree[node][1])

# postorder: 왼쪽 -> 오른쪽 -> 루트 
def postorder(node):
    if node:
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end = "")

n = int(input())

for _ in range(n):
    node, left, right = input().split()
    tree[node] = (left if left != '.' else None, right if right != '.' else None)
    
preorder('A')
print()
inorder('A')
print()
postorder('A')
print()