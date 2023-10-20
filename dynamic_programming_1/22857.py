N, K = map(int, input().split())
S = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(K+1):
        if S[i] % 2 == 0:
            dp[i][j] = dp[i-1][j] + 1
        elif j != 0 and S[i] % 2 == 1:
            dp[i][j] = dp[i-1][j-1]

result = []
for i in dp:
    result.append(i[K])

print(max(result))