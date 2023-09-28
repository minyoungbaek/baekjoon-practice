T = int(input())
dp = [[0] * 30 for _ in range(30)]
for i in range(1, 30):
    dp[i][i] = 1
for i in range(2, 30):
    dp[1][i] = i
for i in range(2, 30):
    for j in range(3, 30):
        dp[i][j] = dp[i][j-1] + dp[i-1][j-1]

for _ in range(T):
    N, M = map(int, input().split())
    print(dp[N][M])