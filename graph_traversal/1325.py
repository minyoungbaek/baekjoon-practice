import sys
from collections import deque
input=sys.stdin.readline

def bfs(graph, start):
    cnt = 1
    queue = deque([start])
    visited = [False for _ in range(N+1)]
    visited[start] = True
    while queue:
        cur = queue.popleft()
        for node in graph[cur]:
            if not visited[node]:
                visited[node] = True
                cnt += 1
                queue.append(node)
    return cnt

N, M = map(int, input().split())
graph = [[] for i in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[v].append(u)

maxCnt = 1
result = []
for i in range(1, N+1):
    cnt = bfs(graph, i)
    if cnt > maxCnt:
        maxCnt = cnt
        result = []
        result.append(i)
    elif cnt == maxCnt:
        result.append(i)

print(*result)