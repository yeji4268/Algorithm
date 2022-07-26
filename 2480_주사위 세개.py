a, b, c = map(int, input().split())
num = [a, b, c]
cnt = list()
money = 0
cnt.append(num.count(num[0]))
cnt.append(num.count(num[1]))
cnt.append(num.count(num[2]))

m = cnt.index(max(cnt))
if max(cnt) == 3:
    money = 10000 + num[m] * 1000
elif max(cnt) == 2:
    money = 1000 + num[m] * 100
else:
    money = max(num) * 100
print(money)
