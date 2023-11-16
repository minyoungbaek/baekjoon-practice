N = int(input())
result = 0
for i in range(1, N+1):
    temp = i + sum(map(int, str(i)))
    if temp == N:
        result = i
        break

print(result)