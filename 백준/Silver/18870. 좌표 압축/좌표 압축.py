import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
nums_2 = sorted(list(set(nums)))

dict = {nums_2[i]: i for i in range(len(nums_2))}

for n in nums:
    print(dict[n], end = ' ')