N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))
zero, one, minus = 0, 0, 0

def dfs(x, y, size):
    global zero, one, minus
    head = paper[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if paper[i][j] != head:
                third = size//3
                dfs(x, y, third)
                dfs(x+third, y, third)
                dfs(x+(2*third), y, third)
                dfs(x, y+third, third)
                dfs(x+third, y+third, third)
                dfs(x+(2*third), y+third, third)
                dfs(x, y+(2*third), third)
                dfs(x+third, y+(2*third), third)
                dfs(x+(2*third), y+(2*third), third)
                return
    if head == -1:
        minus += 1
    elif head == 0:
        zero += 1
    else:
        one += 1

dfs(0, 0, N)
print(minus)
print(zero)
print(one)