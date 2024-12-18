def fibonacci(num):
    zero = [0] * 41
    one = [0] * 41
    
    zero[0], one[0] = 1, 0
    zero[1], one[1] = 0, 1
    
    for i in range(2, num+1):
        zero[i] = zero[i-1] + zero[i-2]
        one[i] = one[i-1] + one[i-2]
    
    return zero[num], one[num]
    
T = int(input())

for _ in range(T):
    num = int(input())
    zero, one = fibonacci(num)
    print(zero, one)