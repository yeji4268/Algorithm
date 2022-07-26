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

N = int(input())
i = 0 
nums = [0, 1]
cnt = 0 
while cnt != N:
    num = nums[i] + nums[i+1]
    nums.append(num)
    i += 1
    cnt += 1
print(nums[N])


