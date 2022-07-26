while True:
    a, b, c = map(int, input().split())
    num = [a, b, c]
    if a + b + c == 0:
        break
    m = max(num)
    num.pop(num.index(m))
    if num[0]**2 + num[1]**2 == m**2:
        print("right")
    else:
        print("wrong")
