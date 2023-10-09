import sys
from collections import deque

def bfs(graph, start):
    queue = deque()
    cnt = 1
    queue.append(start)
    while queue:
        node = queue[0]
        queue.popleft()
        if visited[node] == 0:
            visited[node] = cnt
            cnt += 1
            queue.extend(graph[node])

N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for i in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
for arr in graph:
    arr.sort(reverse=True)

visited = [0]*(N+1)
bfs(graph, R)

for i in range(1, N+1):
    print(visited[i])