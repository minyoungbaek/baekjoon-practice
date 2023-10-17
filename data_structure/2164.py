import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque(range(1,N+1))
while N > 1:
    queue.popleft()
    N -= 1
    queue.append(queue.popleft())
print(queue[0])