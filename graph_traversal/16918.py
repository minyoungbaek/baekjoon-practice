from collections import deque
R,C,N = map(int, input().split())
grid = []
queue = deque()
for _ in range(R):
    grid.append(list(input()))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(queue,grid):
    while queue:
        x,y = queue.popleft()
        grid[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<R and 0<=ny<C and grid[nx][ny]=='O':
                grid[nx][ny] = '.'

def simulate(time):
    global grid, queue
    if time == 1:
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 'O':
                    queue.append((i,j))
    elif time % 2 == 1:
        bfs(queue,grid)
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 'O':
                    queue.append((i,j))
    else:
        grid = [['O']*C for _ in range(R)]

for i in range(1, N+1):
    simulate(i)

for row in grid:
    print(''.join(row))