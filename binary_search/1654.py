K, N = map(int, input().split())
cables = []
for _ in range(K):
    cables.append(int(input()))

left, right = 1, max(cables)
result = 0

while left <= right:
    mid = (left+right) // 2
    total = 0
    for i in range(K):
        total += cables[i] // mid
    if total < N:
        right = mid-1
    else:
        left = mid+1
        result = mid

print(result)