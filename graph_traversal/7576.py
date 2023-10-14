from collections import deque

dx=[0,0,1,-1]
dy=[1,-1,0,0]

M, N = map(int, input().split())
box = []
for _ in range(N):
    box.append(list(map(int, input().split(' '))))

days = -1
queue = deque()
for x in range(N):
    for y in range(M):
        if box[x][y] == 1:
            queue.append((x,y))
queue.append((-1, -1))
while queue:
    x, y = queue.popleft()
    if (x, y) == (-1, -1):
        days += 1
        queue.append((-1, -1))
        x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if box[nx][ny] == 0:
                queue.append((nx, ny))
                box[nx][ny] = 1
for x in range(N):
    for y in range(M):
        if box[x][y] == 0:
            print(-1)
            exit()
print(days)