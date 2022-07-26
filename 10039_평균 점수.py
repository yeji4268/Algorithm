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

scores = list()
for _ in range(5):
    score = int(input())
    if score < 40:
        scores.append(40)
    else:
        scores.append(score)
print(sum(scores)//5)
