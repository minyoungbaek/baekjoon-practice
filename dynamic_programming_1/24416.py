def fib(n):
    global count1
    if n == 1 or n == 2:
        count1 += 1
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib2(n):
    global count2
    f = [0] * (n+1)
    f[1] = 1
    f[2] = 1
    for i in range(3, n+1):
        count2 += 1
        f[i] = f[i-1] + f[i-2]
    return f[n]

n = int(input())
count1 = 0
count2 = 0
fib(n)
fib2(n)
print(count1, count2)