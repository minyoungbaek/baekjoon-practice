import sys
input = sys.stdin.readline

n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

time = 0
if cranes[0] < boxes[0]:
    print(-1)
    exit(0)

while boxes:
    for crane in cranes:
        if boxes and crane < boxes[-1]:
            continue
        for box in boxes:
            if crane >= box:
                boxes.remove(box)
                break
    time += 1

print(time)