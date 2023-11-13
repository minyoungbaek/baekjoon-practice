import sys
import heapq
input = sys.stdin.readline

heap = []

N = int(input())

for _ in range(N):
    nums = list(map(int, input().split()))
    for num in nums:
        if len(heap) == N:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        else:
            heapq.heappush(heap, num)
print(heap[0])