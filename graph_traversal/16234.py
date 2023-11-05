from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a,b):
    visited[a][b] = True
    queue = deque()
    countries = []
    queue.append((a,b))
    countries.append((a,b))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
                if L <= abs(A[nx][ny] - A[x][y]) <= R:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    countries.append((nx,ny))
    return countries

N, L, R = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

days = 0
while True:
    visited = [[False] * N for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                countries = bfs(i,j)
                total = 0
                if len(countries) > 1:
                    flag = 1
                for x,y in countries:
                    total += A[x][y]
                for x,y in countries:
                    A[x][y] = total // len(countries)
    if flag == 0:
        break
    days += 1

print(days)