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

n = int(input())
nums = list()
fac = 2
while(fac ** 2 <= n):
    while n % fac == 0:
        nums.append(fac)
        n = n // fac
    fac += 1
if n > 1:
    nums.append(n)
for num in nums:
    print(num)
