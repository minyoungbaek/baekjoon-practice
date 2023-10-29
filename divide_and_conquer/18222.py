k = int(input())

def thue_morse(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n % 2 == 0:
        return thue_morse(n//2)
    else:
        return 1 - thue_morse(n//2)

print(thue_morse(k-1))