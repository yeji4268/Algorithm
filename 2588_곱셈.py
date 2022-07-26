# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
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
# -


