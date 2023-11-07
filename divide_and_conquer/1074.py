import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())
count = 0

def quad(x, y, size):
    global count
    if x == r and y == c:
        print(count)
        exit(0)
    if size == 1:
        count += 1
        return
    if not (x<=r<x+size and y<=c<y+size):
        count += size * size
        return
    half = size // 2
    quad(x, y, half)
    quad(x, y+half, half)
    quad(x+half, y, half)
    quad(x+half, y+half, half)

quad(0, 0, 2**N)