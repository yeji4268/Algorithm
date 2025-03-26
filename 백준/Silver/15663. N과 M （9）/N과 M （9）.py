import itertools 

N, M = map(int, input().split())
nums = list((map(int, input().split())))
nums = sorted(nums)
perm = list(itertools.permutations(nums, M))
perm = list(set(perm))
perm = sorted(perm)
for p in perm:
    for i in range(M):
        print(p[i], end = ' ')
    print()