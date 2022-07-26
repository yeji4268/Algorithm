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

N = int(input())
num = list(map(int, input().split()))
max = max(num)
sum = 0
for i in range(N):
    num[i] = num[i] / max * 100
    sum = sum + num[i]
print(sum/N)
