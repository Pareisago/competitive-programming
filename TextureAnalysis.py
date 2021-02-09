import fileinput

file = fileinput.input('test.txt')

i = 1
star = 0
dot = 0
for line in file:
    line = line.strip()
    if line == "END":
        exit()
    reversed_line = line[::-1]
    for char in line:
        if char == "*":
            star += 1
        else:
            dot += 1
    if star % dot == 0 or dot % star == 0:
        if line == reversed_line:
            print(i, "EVEN")
    else:
            print(i, "NOT EVEN")
    i += 1