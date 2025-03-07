import sys
import heapq

heap = list()
n = int(sys.stdin.readline().strip())

for _ in range(n):
    x = int(sys.stdin.readline().strip())

    if x > 0:
        heapq.heappush(heap, x) 
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)