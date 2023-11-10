N = int(input())
small = [0]
big = [0]
for i in range(N-1):
    a, b = map(int, input().split())
    small.append(a)
    big.append(b)
k = int(input())

if N == 1:
    print(0)
    exit(0)
elif N == 2:
    print(small[1])
    exit(0)
elif N >= 3:
    dp1 = [0] * (N+1)
    dp1[2] = small[1]
    dp1[3] = min(small[1]+small[2],big[1])
    for i in range(4, N+1):
        dp1[i] = min(dp1[i-1] + small[i-1], dp1[i-2] + big[i-2])
    result = [dp1[N]]
    dp2 = dp1[:]
    for i in range(1, N-2):
        dp2[i+3] = dp1[i] + k
        for j in range(i+4, N+1):
            dp2[j] = min(dp1[j], dp2[j-1] + small[j-1], dp2[j-2] + big[j-2])
        result.append(dp2[N])
    print(min(result))