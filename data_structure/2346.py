from collections import deque
N = int(input())
dq = deque(enumerate(map(int, input().split())))
result = []

while dq:
    idx, count = dq.popleft()
    result.append(idx+1)
    if count > 0:
        dq.rotate(-(count - 1))
    else:
        dq.rotate(-count)

for i in range(N):
    print(result[i], end=' ')