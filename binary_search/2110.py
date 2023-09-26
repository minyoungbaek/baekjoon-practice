import sys
input = sys.stdin.readline

N, C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))

houses.sort()
left = 1
right = houses[-1] - houses[0]
result = 0

while left <= right:
    mid = (left+right) // 2
    ptr = 0
    count = 1
    for i in range(1, N):
        if houses[i] - houses[ptr] >= mid:
            count += 1
            ptr = i
    if count >= C:
        if result < mid:
            result = mid
        left = mid+1
    else:
        right = mid-1
print(result)