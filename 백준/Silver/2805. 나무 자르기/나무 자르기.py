# 이진 탐색(binary search)
def cal_wood(tress, height):
    return sum(max(0, tree - height) for tree in trees)
    
def binary_search(trees, M):
    left, right = 0, max(trees)
    ans = 0
    
    while left <= right:
        mid = (left + right) // 2
        
        wood = cal_wood(trees, mid)
        
        if wood >= M:
            ans = mid
            left = mid + 1 
        else:
            right = mid - 1 
    return ans 

N, M = map(int, input().split())
trees = list(map(int, input().split()))

print(binary_search(trees, M))