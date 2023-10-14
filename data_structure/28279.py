import sys
from collections import deque
input=sys.stdin.readline

dq = deque()

N = int(input())
for _ in range(N):
    s = input().split()
    f = len(dq)
    if s[0] == '1':
        dq.appendleft(s[1])
    elif s[0] == '2':
        dq.append(s[1])
    elif s[0] == '3':
        print(dq.popleft() if f else -1)
    elif s[0] == '4':
        print(dq.pop() if f else -1)
    elif s[0] == '5':
        print(len(dq))
    elif s[0] == '6':
        print(0 if f else 1)
    elif s[0] == '7':
        print(dq[0] if f else -1)
    elif s[0] == '8':
        print(dq[-1] if f else -1)