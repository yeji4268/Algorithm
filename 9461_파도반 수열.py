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

t = int(input())
num = [1, 1, 1, 2, 2]
for i in range(5, 100):
    num.append(num[i-1]+ num[i-5])
for _ in range(t):
    n = int(input())
    print(num[n-1])


