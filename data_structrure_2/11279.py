import sys
import heapq
input = sys.stdin.readline

hq = []

N = int(input())
for _ in range(N):
    x = int(input())
    if x == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(heapq.heappop(hq) * -1)
    else:
        heapq.heappush(hq, x*-1)