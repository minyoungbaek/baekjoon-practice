import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def dfs_recursive(graph, start, parent):
    for node in graph[start]:
        if parent[node] == 0:
            parent[node] = start
            dfs_recursive(graph, node, parent)

N = int(input())
graph = [[] for i in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

parent = [0]*(N+1)
dfs_recursive(graph, 1, parent)

for i in range(2, N+1):
    print(parent[i])