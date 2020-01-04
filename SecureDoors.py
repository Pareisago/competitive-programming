import fileinput

file = fileinput.input()

logs = int(file.readline())
i = 0
names = []

while i < logs:
    line = file.readline()
    line = line.strip().split()
    if line[0] == 'entry':
        if line[1] not in names:
            print(line[1] + ' entered')
            names.append(line[1])
        else:
            print(line[1] + ' entered (ANOMALY)')
    elif line[0] == 'exit':
        if line[1] in names:
            print(line[1] + ' exited')
            names.remove(line[1])
        else:
            print(line[1] + ' exited (ANOMALY)')
    i += 1