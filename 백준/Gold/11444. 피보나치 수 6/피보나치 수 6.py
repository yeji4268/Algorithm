MOD = 1_000_000_007

def fib(n):
    def helper(n):
        if n == 0:
            return (0, 1)
        a, b = helper(n // 2)
        c = (a * ((2 * b - a) % MOD)) % MOD
        d = (a * a + b * b) % MOD
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, (c + d) % MOD)

    return helper(n)[0]

n = int(input())
print(fib(n))