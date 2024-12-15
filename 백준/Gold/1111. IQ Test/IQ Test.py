import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
 
if N == 1: 
    print('A')
elif N == 2:
    if nums[0] == nums[1]: 
        print(nums[0])
    else: 
        print('A')
else:
    if nums[1] - nums[0] != 0:
        a = (nums[2] - nums[1]) // (nums[1] - nums[0])
    else: 
        a = 0
 
    b = nums[1] - a * nums[0]
    flag = 0
    for j in range(N - 1):
        res = a * nums[j] + b
        if nums[j + 1] == res:
            continue
        else:
            print('B')
            flag = 1
            break
    
    if flag != 1:
        print(nums[N - 1] * a + b)
