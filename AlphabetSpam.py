import fileinput

file = fileinput.input("test.txt")

line = file.readline()

count = len(line)
symbols = 0

for char in line:
    a = ord(char)
    if a < 48:
        symbols += 1
    if 57 < a < 65:
        symbols += 1
    if 90 < a < 95:
        symbols += 1
    if a == 96:
        symbols += 1
    if a > 122:
        symbols += 1

print(symbols/count)