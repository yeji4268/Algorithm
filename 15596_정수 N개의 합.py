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

def solve(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum 
nums = [1, 2, 3, 4, 5]
print(solve(nums))

