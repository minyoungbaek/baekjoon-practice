N = int(input())
exp = input()
num = []
for _ in range(N):
    num.append(int(input()))

stack = []
for i in exp:
    if 'A' <= i <= 'Z':
        stack.append(num[ord(i)-ord('A')])
    else:
        str2 = stack.pop()
        str1 = stack.pop()
        if i == '+':
            stack.append(str1+str2)
        elif i == '-':
            stack.append(str1-str2)
        elif i == '*':
            stack.append(str1*str2)
        elif i == '/':
            stack.append(str1/str2)

print('%.2f' %stack[0])