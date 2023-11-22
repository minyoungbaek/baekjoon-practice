board = []
result = []
N, M = map(int, input().split())

for row in range(N):
    row = input()
    board.append(row)

for i in range(N-7):
    for j in range(M-7):
        case1 = 0
        case2 = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y) % 2 == 0:
                    if board[x][y] != 'B':
                        case1 += 1
                    if board[x][y] != 'W':
                        case2 +=1
                else:
                    if board[x][y] != 'W':
                        case1 += 1
                    if board[x][y] != 'B':
                        case2 += 1
        result.append(case1)
        result.append(case2)

print(min(result))