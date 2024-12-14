from itertools import product

n, k = map(int, input().split())
len_n = len(str(n))
nums = list(input().split())

while True:
    p = list(product(nums, repeat = len_n)) 
    res = []

    for i in p:
        if int("".join(i)) <= n:
            res.append(int("".join(i)))
    
    if len(res) >= 1:
        print(max(res))
        break
    else:
        len_n -= 1