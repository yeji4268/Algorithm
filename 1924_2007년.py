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
day = 0 
dayList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekList = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

x, y = map(int, input().split())

for i in range(x-1):
    day = day + dayList[i]
day = (day + y) % 7
print(weekList[day])
