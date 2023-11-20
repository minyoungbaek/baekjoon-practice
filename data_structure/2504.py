str = input()
stack = []
result = 0
num = 1
for i in range(len(str)):
    if str[i] == '(':
        stack.append(str[i])
        num *= 2
    elif str[i] == '[':
        stack.append(str[i])
        num *= 3
    elif str[i] == ')':
        if not stack or stack[-1] != '(':
            result = 0
            break
        if str[i-1] == '(':
            result += num
        stack.pop()
        num //= 2
    elif str[i] == ']':
        if not stack or stack[-1] != '[':
            result = 0
            break
        if str[i-1] == '[':
            result += num
        stack.pop()
        num //= 3

if stack:
    print(0)
else:
    print(result)