import fileinput

file = fileinput.input()
line = file.readline()
line = line.rstrip().split()

A = 1
B = 0
C = 0

for char in line[0]:
    if char == 'A':
        if A == 0:
            if B == 0:
                continue
        if A == 1:
            if B == 0:
                B = 1
                A = 0
                continue
        if A == 0:
            if B == 1:
                A = 1
                B = 0
                continue
    if char == 'B':
        if B == 0:
            if C == 0:
                continue
        if B == 1:
            if C == 0:
                B = 0
                C = 1
                continue
        if B == 0:
            if C == 1:
                B = 1
                C = 0
                continue
    if char == 'C':
        if C == 0:
            if A == 0:
                continue
        if C == 0:
            if A == 1:
                C = 1
                A = 0
                continue
        if A == 0:
            if C == 1:
                C = 0
                A = 1
                continue


if A == 1:
    print("1")
if B == 1:
    print("2")
if C == 1:
    print("3")