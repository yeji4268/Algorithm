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
M = int(input())
N = int(input())

prime = list()
for i in range(M, N +1):
    for j in range(2, i + 1):
        if j == i :
            prime.append(i)
        if i % j == 0:
            break
            
if not prime:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))
# -


