import fileinput

list = ''
for line in fileinput.input('test.txt'):
    line = line.strip().split()
    for item in line:
        list = list + item[0]

print(list)
i = 0
for char in list:
    if char[i] == char[i+1]:
    print(char)