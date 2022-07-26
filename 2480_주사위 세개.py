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
