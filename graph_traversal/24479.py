import sys
sys.setrecursionlimit(10 ** 6)

def dfs_recursive(graph, start, visited):
    global cnt
    visited[start] = cnt
    for node in graph[start]:
        if visited[node] == 0:
            cnt += 1
            dfs_recursive(graph, node, visited)

N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for i in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
for arr in graph:
    arr.sort()

visited = [0]*(N+1)
cnt = 1
dfs_recursive(graph, R, visited)

for i in range(1, N+1):
    print(visited[i])