scores = list()
for _ in range(5):
    score = int(input())
    if score < 40:
        scores.append(40)
    else:
        scores.append(score)
print(sum(scores)//5)
