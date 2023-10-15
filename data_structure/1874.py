count = 1
temp = True
stack = []
arr = []

N = int(input())
for i in range(N):
    num = int(input())
    while count <= num:
        stack.append(count)
        arr.append('+')
        count += 1
    if stack[-1] == num:
        stack.pop()
        arr.append('-')
    else:
        temp = False
        break

if temp == False:
    print('NO')
else:
    for sign in arr:
        print(sign)