from collections import deque
queue = deque()

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(start):
    queue.append(start)
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and visited[nx][ny] == -1:
                if map[nx][ny] == 0:
                    visited[nx][ny] = 0
                elif map[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))

N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if map[i][j] == 2:
            start = (i,j)
            visited[i][j] = 0

bfs(start)

for i in range(N):
    for j in range(M):
        if map[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()