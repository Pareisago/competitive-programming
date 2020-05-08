import fileinput

file = fileinput.input()

free_days = set()
line1 = file.readline()

for line in file:
    line = line.strip().split()
    i = int(line[0])
    while i <= int(line[1]):
        free_days.add(i)
        i += 1

print(len(free_days))
