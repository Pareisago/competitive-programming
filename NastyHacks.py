import fileinput

file = fileinput.input()
line = file.readline()
line = line.strip().split()
reps = int(line[0])
i = 0
while i < reps:
    line = file.readline()
    line = line.strip().split()
    diff = int(line[1]) - int(line[0])
    if diff > int(line[2]):
        print("advertise")
    if diff < int(line[2]):
        print("do not advertise")
    if diff == int(line[2]):
        print("does not matter")
    i += 1
