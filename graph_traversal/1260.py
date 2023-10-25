import sys
sys.setrecursionlimit(10 ** 6)
from collections import deque

def dfs(graph, start):
    visited_dfs.append(start)
    for node in graph[start]:
        if node not in visited_dfs:
            dfs(graph, node)

def bfs(graph, start):
    queue = deque()
    queue.append(start)
    while queue:
        node = queue[0]
        queue.popleft()
        if node not in visited_bfs:
            visited_bfs.append(node)
            queue.extend(graph[node])

N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for i in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
for arr in graph:
    arr.sort()

visited_dfs = []
visited_bfs = []
dfs(graph, V)
bfs(graph, V)
print(*visited_dfs)
print(*visited_bfs)