N, K = map(int, input().split())
kids = list(map(int, input().split()))
diff = []

for i in range(1, N):
    diff.append(kids[i]-kids[i-1])
diff.sort()
cost = 0
for i in range(N-K):
    cost += diff[i]

print(cost)