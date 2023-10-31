exp = input()
stack = []
total = 0
for i in range(len(exp)):
    if exp[i] == '(':
        stack.append('(')
    else:
        if exp[i-1] == '(':
            stack.pop()
            total += len(stack)
        else:
            stack.pop()
            total += 1
print(total)