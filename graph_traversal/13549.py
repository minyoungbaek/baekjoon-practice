from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque()
visited = [-1] * 100001
visited[n] = 0

queue.append(n)
while queue:
    s = queue.popleft()
    if s == k:
        print(visited[s])
        break
    if 0 <= s-1 < 100001 and visited[s-1] == -1:
        queue.append(s-1)
        visited[s-1] = visited[s] + 1
    if 0 <= s*2 < 100001 and visited[s*2] == -1:
        queue.appendleft(s*2)
        visited[s*2] = visited[s]
    if 0 <= s+1 < 100001 and visited[s+1] == -1:
        queue.append(s+1)
        visited[s+1] = visited[s] + 1