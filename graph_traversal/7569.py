from collections import deque

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

M, N, H = map(int, input().split())
boxes = []
for _ in range(H):
    box = []
    for _ in range(N):
        box.append(list(map(int, input().split(' '))))
    boxes.append(box)

days = -1
queue = deque()
for x in range(H):
    for y in range(N):
        for z in range(M):
            if boxes[x][y][z] == 1:
                queue.append((x,y,z))
queue.append((-1,-1,-1))
while queue:
    x,y,z = queue.popleft()
    if (x,y,z) == (-1,-1,-1):
        days += 1
        queue.append((-1,-1,-1))
        x,y,z = queue.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M:
            if boxes[nx][ny][nz] == 0:
                boxes[nx][ny][nz] = 1
                queue.append((nx,ny,nz))
for x in range(H):
    for y in range(N):
        for z in range(M):
            if boxes[x][y][z] == 0:
                print(-1)
                exit()
print(days)