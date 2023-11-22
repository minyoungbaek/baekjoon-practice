import sys
input = sys.stdin.readline

N, M = map(int, input().split())
T = []
for _ in range(N):
    T.append(int(input()))

left = min(T)
answer = right = max(T) * M

while left <= right:
    total = 0
    mid = (left + right) // 2
    for i in range(N):
        total += mid // T[i]
    if total >= M:
        right = mid - 1
        answer = min(answer, mid)
    else:
        left = mid + 1

print(answer)