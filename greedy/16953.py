A, B = map(int, input().split())

count = 1
while True:
    if B == A:
        print(count)
        break
    elif (B % 2 != 0 and B % 10 != 1) or (B < A):
        print(-1)
        break
    else:
        if B % 2 == 0:
            B = B // 2
            count += 1
        elif B % 10 == 1:
            B = B // 10
            count += 1