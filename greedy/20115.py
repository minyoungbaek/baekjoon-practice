N = int(input())
drinks = list(map(int, input().split()))
drinks.sort()

for i in range(N-1):
    drinks[-1] = drinks[-1] + (drinks[i]/2)

print(drinks[-1])