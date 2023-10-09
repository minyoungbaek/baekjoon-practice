import sys
from collections import deque
input=sys.stdin.readline

N, K = map(int, input().split())
queue = deque(range(1, N+1))
answer = []

while queue:
    for _ in range(K-1):
        queue.append(queue.popleft())
    answer.append(str(queue.popleft()))
print('<',', '.join(answer),'>', sep='')