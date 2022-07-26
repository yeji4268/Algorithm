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
cnt = 0
origin = N

while True:
    a = N // 10  
    b = N % 10
    c = (a + b) // 10
    d = (a + b) % 10
    N = b * 10 + d
    cnt = cnt + 1
    
    if N == origin :
        break
print(cnt)
# -


