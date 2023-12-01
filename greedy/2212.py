import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensors = list(map(int, input().split()))
sensors.sort()

if k >= n:
    print(0)
    exit(0)

diff = []
for i in range(1, n):
    diff.append(sensors[i]-sensors[i-1])
diff.sort(reverse=True)

for _ in range(k-1):
    diff.pop(0)

print(sum(diff))