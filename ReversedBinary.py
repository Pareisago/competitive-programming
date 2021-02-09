import fileinput

file = fileinput.input("test.txt")
line = file.readline()
line = line.strip().split()

binary = bin(int(line[0]))
binary = binary[2::]
reversed = binary[::-1]

print(int(reversed, 2))