import fileinput

file = fileinput.input()
line = file.readline()

myset = set()

i = 0
while i < len(line):
    try:
        myset.add(line[i])
        myset.add(line[i+1])
        myset.add(line[i+2])
    except Exception:
        myset.clear()
        pass
    if 'R' in myset:
        if 'B' in myset:
            if 'L' in myset:
                print('C', end='')
                i += 3
                myset.clear()
                continue
    myset.clear()
    if line[i] == 'R':
        print('S', end='')
    if line[i] == 'B':
        print('K', end='')
    if line[i] == 'L':
        print('H', end='')
    i += 1