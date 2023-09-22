N = int(input())
image = []
for _ in range(N):
    image.append(list(map(int, input().split())))
result = []

def quadtree(x, y, size):
    global result
    head = image[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if image[i][j] != head:
                result.append("(")
                half = size//2
                quadtree(x, y, half)
                quadtree(x, y+half, half)
                quadtree(x+half, y, half)
                quadtree(x+half, y+half, half)
                result.append(")")
                return
    result.append(head)

quadtree(0, 0, N)
print("".join(map(str,(result)))