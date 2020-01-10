import fileinput

file = fileinput.input()

for line in file:
    line = line.lower()
    line = line.strip().split()
    a = 0
    for item in line:
        if 'problem' in item:
            a += 1
        else:
            a += 0
    if a >= 1:
        print('yes')
    else:
        print('no')
