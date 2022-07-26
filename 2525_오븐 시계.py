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
h, m = map(int, input().split())
time = int(input()) 

h += time // 60
m += time % 60

if m >= 60:
    h += 1
    m -= 60
if h >= 24:
    h -= 24

print(h, m)
# -


