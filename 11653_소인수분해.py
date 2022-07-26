n = int(input())
nums = list()
fac = 2
while(fac ** 2 <= n):
    while n % fac == 0:
        nums.append(fac)
        n = n // fac
    fac += 1
if n > 1:
    nums.append(n)
for num in nums:
    print(num)
