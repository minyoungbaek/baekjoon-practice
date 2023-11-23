import heapq
import sys
input = sys.stdin.readline

N = int(input())
time = []
for _ in range(N):
    time.append(list(map(int, input().split())))

time.sort()

heap = []
for start, end in time:
    if heap and heap[0] <= start:
        heapq.heappop(heap)
    heapq.heappush(heap, end)

print(len(heap)) 