from itertools import combinations

n = int(input())
nums = list()      

for i in range(1, 11):     
    for c in combinations(range(0, 10), i):  
        c = list(c)
        c.sort(reverse=True)                   
        nums.append(int("".join(map(str, c))))

nums.sort() 

try:
    print(nums[n - 1])
except: 
    print(-1)
