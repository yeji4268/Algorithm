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
N = int(input())

for i in range(N):
    A, B = map(int, input().split())
    print(f"Case #{i + 1}: {A} + {B} = {A+B}")
# -


