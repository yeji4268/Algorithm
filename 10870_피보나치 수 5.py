N = int(input())
i = 0 
nums = [0, 1]
cnt = 0 
while cnt != N:
    num = nums[i] + nums[i+1]
    nums.append(num)
    i += 1
    cnt += 1
print(nums[N])
