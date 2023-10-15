import sys
sys.setrecursionlimit(10 ** 6)

def dfs(start):
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            dfs(node)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for i in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = []
dfs(1)
print(len(visited)-1)