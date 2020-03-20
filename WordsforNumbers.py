import fileinput

file = fileinput.input("test.txt")
line = file.readline()

print(line)