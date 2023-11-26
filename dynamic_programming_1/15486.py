import sys
input = sys.stdin.readline

N = int(input())
t = [0]
p = [0]
for _ in range(N):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

dp = [0] * (N+1)
for i in range(1, N+1):
    dp[i] = max(dp[i], dp[i-1])
    date = i + t[i] - 1
    if date <= N:
        dp[date] = max(dp[date], dp[i-1]+p[i])

print(max(dp))