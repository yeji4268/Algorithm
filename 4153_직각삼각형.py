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

while True:
    a, b, c = map(int, input().split())
    num = [a, b, c]
    if a + b + c == 0:
        break
    m = max(num)
    num.pop(num.index(m))
    if num[0]**2 + num[1]**2 == m**2:
        print("right")
    else:
        print("wrong")


