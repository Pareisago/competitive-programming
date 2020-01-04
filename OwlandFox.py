import fileinput

file = fileinput.input("test.txt")
num = int(file.readline())

i = 0
while i < num:
    line = file.readline()
    line = line.strip().split()
    count = len(line[0])
    q = 0
    while q < count:
        if int(line[0][q]) == '1':
            q += 1
        else:
            num = int(line[0][q])
            num -= 1
            line[0][q] = num
        q += 1
    print(line)
    i += 1
