import sys
from collections import deque
T = int(sys.stdin.readline())
dic = {}
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    rank = list(map(int, sys.stdin.readline().split()))
    docs = list(map(chr, range(97, 97+N)))
    qu = deque(docs)
    for i in range(N):
        dic[docs[i]] = rank[i]
    printer = 0
    order = 0
    while True:
        while True:
            flag = 0
            for i in range(1, len(qu)):
                if dic[qu[0]] < dic[qu[i]]:
                    qu.append(qu.popleft())
                    flag = 1
                    break
            if flag == 0:
                break
        printer = qu[0]
        order += 1
        qu.popleft()
        if printer == docs[M]:
            break
    print(order)