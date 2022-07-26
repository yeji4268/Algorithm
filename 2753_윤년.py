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

year = int(input())
if(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
    print(1)
else :
    print(0)


