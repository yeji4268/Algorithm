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

A, B = input().split()
listA, listB = list(A), list(B)
numA = int(listA[2]) * 100 + int(listA[1]) * 10 + int(listA[0])
numB = int(listB[2]) * 100 + int(listB[1]) * 10 + int(listB[0])
ans = numA if numA > numB else numB
print(ans)


