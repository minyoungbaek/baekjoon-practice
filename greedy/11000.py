import sys
import heapq
input = sys.stdin.readline

N = int(input())
time = []
for _ in range(N):
    time.append(list(map(int, input().split())))
time.sort()

heap = []
heapq.heappush(heap, time[0][1])
for i in range(1, N):
    if time[i][0] >= heap[0]:
        heapq.heappop(heap)
    heapq.heappush(heap, time[i][1])

print(len(heap))