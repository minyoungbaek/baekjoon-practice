N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for x in range(N):
    for y in range(N):
        if x == y == N-1:
            print(dp[x][y])
            exit(0)
        dist = board[x][y]
        if 0 <= x+dist < N:
            dp[x+dist][y] += dp[x][y]
        if 0 <= y+dist < N:
            dp[x][y+dist] += dp[x][y]