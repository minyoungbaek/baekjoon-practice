n = int(input())
num = list(map(int, input().split()))
total = [0] * n
total[0] = num[0]
for i in range(1, n):
    total[i] = max(num[i], total[i-1]+num[i])
print(max(total))