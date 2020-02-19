import fileinput

file = fileinput.input()
commands = int(file.readline())


i = 0
for line in file:
    if i <= commands:
        if line[0:10] == 'Simon says':
            print(line[11::], end='')
        i += 1

