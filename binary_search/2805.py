N, M = map(int, input().split())
trees = list(map(int, input().split()))

H, L = max(trees), 0
result = 0

while L <= H:
    mid = (H+L) // 2
    total = 0
    for tree in trees:
        if tree >= mid:
            total += tree - mid
    if total < M:
        H = mid-1
    else:
        L = mid+1
        result = mid

print(result)