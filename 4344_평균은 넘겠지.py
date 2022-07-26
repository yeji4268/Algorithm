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
C = int(input())

for _ in range(C):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]
    nums = [x for x in nums if x > avg]
    print(f"{len(nums)/nums[0] * 100:.3f}%")
# -


