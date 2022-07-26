C = int(input())

for _ in range(C):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]
    nums = [x for x in nums if x > avg]
    print(f"{len(nums)/nums[0] * 100:.3f}%")
