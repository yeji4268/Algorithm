A, B = input().split()
listA, listB = list(A), list(B)
numA = int(listA[2]) * 100 + int(listA[1]) * 10 + int(listA[0])
numB = int(listB[2]) * 100 + int(listB[1]) * 10 + int(listB[0])
ans = numA if numA > numB else numB
print(ans)
