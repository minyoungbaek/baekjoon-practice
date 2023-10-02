mk = input()
min = ''
max = ''
count = 0
if 'K' not in mk:
    max += '1' * len(mk)
    min = 10 ** (len(mk)-1)
else:
    for x in mk:
        if x == 'K':
            max += str(5*10**(count))
            if count > 0:
                min += str(10**(count-1))
            min += '5'
            count = 0
        else:
            count += 1
    max += '1' * count
    if count > 0:
        min += str(10**(count-1))

print(int(max))
print(int(min))