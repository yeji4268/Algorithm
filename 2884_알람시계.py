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
H, M = map(int, input().split())

if M < 45 :
    if H == 0:
        H = 23
    else :
        H = H - 1
    M = 60 - 45 + M
else:
    M = M - 45

print(H, M)
