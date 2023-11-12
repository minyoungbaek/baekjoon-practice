N, K = map(int, input().split())
rocks = list(map(int, input().split()))

dp = [0] * N
dp[0] = 1
for i in range(N-1):
    if dp[i] == 1:
        for j in range(i+1, i+K+1):
            if j >= N:
                break
            if (j - i) * (1 + abs(rocks[i] - rocks[j])) <= K:
                dp[j] = 1
if dp[N-1] == 1:
    print('YES')
else:
    print('NO')