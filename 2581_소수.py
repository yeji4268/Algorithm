M = int(input())
N = int(input())

prime = list()
for i in range(M, N +1):
    for j in range(2, i + 1):
        if j == i :
            prime.append(i)
        if i % j == 0:
            break
            
if not prime:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))
