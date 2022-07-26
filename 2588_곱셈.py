op1 = int(input())
op2 = int(input())

first = op2 // 100
second = (op2 - first * 100) // 10
third = (op2 - (first* 100 + second * 10))

a = op1 * third
b = op1 * second
c = op1 * first
d = a + b * 10 + c * 100

print(a)
print(b)
print(c)
print(d)
