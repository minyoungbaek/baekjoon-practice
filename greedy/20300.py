N = int(input())
t = list(map(int, input().split()))
plan = []
t.sort()

if N%2 == 1:
    plan.append(t[-1])
    t = t[:-1]
for i in range(len(t)//2):
    plan.append(t[i]+t[len(t)-1-i])
print(max(plan))