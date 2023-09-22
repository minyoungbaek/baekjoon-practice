N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))
w = 0
b = 0

def quadtree(x, y, size):
    global w, b
    head = paper[x][y]
    for dx in range(size):
        for dy in range(size):
            if paper[x+dx][y+dy] != head:
                half = size//2
                quadtree(x, y, half)
                quadtree(x+half, y, half)
                quadtree(x, y+half, half)
                quadtree(x+half, y+half, half)
                return
    if head == 0:
        w += 1
    else:
        b += 1

quadtree(0, 0, N)
print(w)
print(b)