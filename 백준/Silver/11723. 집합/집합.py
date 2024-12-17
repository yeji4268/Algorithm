import sys
input = sys.stdin.readline
M = int(input())
S = set()

for _ in range(M):
    comm = list(input().split())
    
    if len(comm) == 1:
        if comm[0] == "all":
            S = set(list(range(1, 21)))
        else:
            S = set()
    else:
        com, com_num = comm[0], comm[1]
        com_num = int(com_num)

        if com == "add":
            S.add(com_num)
        elif com == "remove":
            S.discard(com_num)
        elif com == "check":
            print(1 if com_num in S else 0)
        elif com == "toggle":
            if com_num in S: 
                S.discard(com_num)
            else: 
                S.add(com_num)