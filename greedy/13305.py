N = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))
total = 0
cur = price[0]

for i in range(N-1):
    if cur > price[i]:
        cur = price[i]
    total += cur * dist[i]

print(total)