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
t = int(input())

for _ in range(t):  
    floor = int(input())
    num = int(input())
    f = [x for x in range(1, num+1)] 
    for k in range(floor):  
        for i in range(1, num): 
            f[i] += f[i-1] 
    print(f[-1]) 
# -


