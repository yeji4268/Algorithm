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

x, y, w, h = map(int, input().split())
dis = list()
dis.append(h-y)
dis.append(w-x)
dis.append(y)
dis.append(x)
print(min(dis))


