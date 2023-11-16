N, M = map(int, input().split())
numbers = list(map(int, input().split()))
sum = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if M >= numbers[i] + numbers[j] + numbers[k] > sum:
                sum = numbers[i] + numbers[j] + numbers[k]
            
print(sum)