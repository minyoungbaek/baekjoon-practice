N = int(input())
if N % 5 == 0:
    print(N//5)
else:
    num = 0
    while N > 0:
        N -= 3
        num += 1
        if N % 5 == 0:
            num += N//5
            print(num)
            break
        elif N == 1 or N == 2:
            print(-1)
            break
        elif N == 0:
            print(num)
            break