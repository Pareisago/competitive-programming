import fileinput

file = fileinput.input('test.txt')

line = file.readline()
line = line.strip()
line = [char for char in line]

zoom = len(line)
x = 0
y = 0

# for i in range(zoom):

print(zoom)