N = int(input())

fileName_1 = list(input())
for _ in range(N-1):
    fileName_2 = list(input())
    for i in range(len(fileName_1)):
        if fileName_1[i] != fileName_2[i]:
            fileName_1[i] = '?'
print(''.join(fileName_1))