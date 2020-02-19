import fileinput

file = fileinput.input()
line = file.readline()
line = line.strip().split()

article = int(line[0])
factor = int(line[1])

out = (factor - 1) * article + 1

print(out)

