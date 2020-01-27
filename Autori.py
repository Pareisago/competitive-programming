import fileinput

file = fileinput.input()

line = file.readline()

word = ''

i = 0
for char in line:
    if i == 0:
        word += line[i]
    if char == '-':
        word += line[i+1]
    i += 1

print(word)
