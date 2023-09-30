eq = input()
new_eq = ['(']
num = []
for i in eq:
    if i == '-':
        new_eq.append(str(int("".join(num))))
        num = []
        new_eq.append(')')
        new_eq.append('-')
        new_eq.append('(')
    elif i == '+':
        new_eq.append(str(int("".join(num))))
        num = []
        new_eq.append('+')
    else:
        num.append(i)
new_eq.append(str(int("".join(num))))
new_eq.append(')')
result = "".join(new_eq)
print(eval(result))