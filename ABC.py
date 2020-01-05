import fileinput

file = fileinput.input()
line = file.readline()
numbers = line.strip().split()
line = file.readline()
letters = line.strip().split()

numbers[0] = int(numbers[0])
numbers[1] = int(numbers[1])
numbers[2] = int(numbers[2])

numbers.sort()

A = numbers[0]
B = numbers[1]
C = numbers[2]

i = 1
for char in str(letters):
    if char == 'A':
        if i != 3:
            print(A, end=' ')
            i += 1
        else:
            print(A)
    if char == 'B':
        if i != 3:
            print(B, end=' ')
            i += 1
        else:
            print(B)
    if char == 'C':
        if i != 3:
            print(C, end=' ')
            i += 1
        else:
            print(C)