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
from math import gcd
def lcm(x, y):
    return x * y // gcd(x, y)

a, b = map(int, input().split())
print(gcd(a, b))
print(lcm(a, b))
        
# -


