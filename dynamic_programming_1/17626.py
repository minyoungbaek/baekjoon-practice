import math

n = int(input())
sq = [i*i for i in range(1, 224)]
dp = [0] * (n+1)

for i in range(1, n+1):
    if i in sq:
        dp[i] = 1
    else:
        dp[i] = min([dp[i-j] for j in sq if i-j > 0])+1

print(dp[n])