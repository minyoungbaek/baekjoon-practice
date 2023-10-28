N = int(input())
first_matrix = []
for _ in range(N):
    first_matrix.append(list(map(int, input().split())))

def pooling(size, matrix):
    if size == 1:
        print(matrix[0][0])
        return
    new_matrix = []
    for i in range(0, size, 2):
        row = []
        for j in range(0, size, 2):
            num = [matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]]
            num.sort(reverse=True)
            row.append(num[1])
        new_matrix.append(row)
    half = size // 2
    pooling(half, new_matrix)

pooling(N, first_matrix)