import sys
input = sys.stdin.readline

N = int(input())
prices = []
for _ in range(N):
    prices.append(int(input()))
prices.sort(reverse=True)

total = 0
for i in range(N):
    if (i+1) % 3 == 0:
        continue
    else:
        total += prices[i]

print(total)