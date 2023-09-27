N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))
coins.reverse()
count = 0
for coin in coins:
    if K == 0:
        break
    count += K // coin
    K %= coin
print(count)