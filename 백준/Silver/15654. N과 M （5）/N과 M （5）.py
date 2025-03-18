def backtrack(arr, path, m):
    if len(path) == m:
        print(' '.join(map(str, path)))
        return 
    for i in range(len(arr)):
        backtrack(arr[:i] + arr[i+1:], path + [arr[i]], m)

n, m = map(int, input().split())
nums = sorted(map(int, input().split()))
backtrack(nums, list(), m)