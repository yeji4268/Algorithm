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
import math
n = int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dis = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if dis == 0 and r1 == r2:
        print(-1)
    elif abs(r1 - r2) == dis or r1 + r2 == dis:
        print(1)
    elif abs(r1 - r2) < dis < (r1+r2):
        print(2)
    else:
        print(0)
