import sys
N, K = map(int, sys.stdin.readline().split)
queue = list(range(1, N+1))
result = []
ptr = 0
for _ in range(N):
    ptr += K-1
    if ptr >= len(queue):
        ptr = ptr%len(queue)
    result.append(queue.pop(ptr))
print('<',', '.join(str(i) for i in result), '>', sep='')