import sys
input = sys.stdin.readline

N = int(input())
stones = [0] + list(map(int, input().split()))
min, max = 1, (N-1) * (1+abs(stones[N]-stones[1]))
result = 0

while min <= max:
    mid = (min + max) // 2
    flag = 0
    stack = [1]
    visited = [False] * (N+1)
    visited[1] = True
    while stack:
        K = stack.pop()

        if K == N:
            flag = 1
            break

        for i in range(K+1, N+1):
            power = (i-K) * (1+abs(stones[i]-stones[K]))
            if power <= mid and not visited[i]:
                stack.append(i)
                visited[i] = True

    if flag:
        max = mid - 1
        result = mid
    else:
        min = mid + 1
    
print(result)