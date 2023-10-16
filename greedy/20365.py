N = int(input())
colors = input()

cdict = {'B':0, 'R':0}
if colors[0] == 'R':
    cdict['R'] += 1
elif colors[0] == 'B':
    cdict['B'] += 1

for i in range(1, N):
    if colors[i] == 'R':
        if colors[i-1] != colors[i]:
            cdict['R'] += 1
    elif colors[i] == 'B':
        if colors[i-1] != colors[i]:
            cdict['B'] += 1

print(min(cdict['R'], cdict['B'])+1)