from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

N, M = map(int, input().split())
maze = []
visited = [[0] * (M+1) for _ in range(N+1)]

for _ in range(N):
    maze.append(list(map(int, input())))

queue = deque()
queue.append((1,1))
visited[1][1] = 1
while queue:
    x, y = queue.popleft()
    if x == N and y == M:
        print(visited[x][y])
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 < nx <= N and 0 < ny <= M:
            if maze[nx-1][ny-1] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))