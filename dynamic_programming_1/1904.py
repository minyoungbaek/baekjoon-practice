N = int(input())
T = [0] * 1000001
T[1] = 1
T[2] = 2

for i in range(3, N+1):
    T[i] = (T[i-1] + T[i-2])%15746

print(T[N])