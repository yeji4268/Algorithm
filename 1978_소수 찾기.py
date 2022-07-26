N = int(input())
cnt = 0
nums = list(map(int, input().split()))
for num in nums:
    for i in range(1, num):
        if(num % i != 0 or num == 1):
            break 
        else:
            cnt = cnt + 1
print(cnt)
