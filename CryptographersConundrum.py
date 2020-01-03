import fileinput

file = fileinput.input()
line = file.readline()
line = line.strip().split()
length = len(line[0])

count = 0
i = 0
# p
while i < length:
    if line[0][i] != 'P':
        count += 1
    i += 3

# e
r = 1
while r < length:
    if line[0][r] != 'E':
        count += 1
    r += 3

# r
m = 2
while m < length:
    if line[0][m] != 'R':
        count += 1
    m += 3

print(count)