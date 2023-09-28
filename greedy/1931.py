N = int(input())
times = []
for _ in range(N):
    i, j = map(int, input().split(" "))
    times.append((i, j))
times.sort(key=lambda x: (x[1], x[0]))

cur = 0
count = 0
for time in times:
    if cur <= time[0]:
        cur = time[1]
        count += 1

print(count)