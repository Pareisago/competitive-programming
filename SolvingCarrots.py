import fileinput
file = fileinput.input()
line = file.readline()
data = line.rstrip().split()

print(data[1])
