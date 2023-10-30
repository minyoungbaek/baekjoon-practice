N = int(input())
tips = []
for _ in range(N):
    tips.append(int(input()))
tips.sort(reverse=True)
total = 0
for i in range(N):
    temp = tips[i] - i
    if temp >= 0:
        total += temp
print(total)