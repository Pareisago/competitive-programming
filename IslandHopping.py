# WORK IN PROGRESS

import fileinput

file = fileinput.input("test.txt")

cases = int(file.readline())

islands = int(file.readline())

q = 0
while q <= cases:
    total = 0
    i = 0
    while i < islands:
        distance = file.readline()
        distance = distance.strip().split()
        x1 = float(distance[0])
        y1 = float(distance[1])
        distance = file.readline()
        distance = distance.strip().split()
        x2 = float(distance[0])
        y2 = float(distance[1])
        x = abs(x1 - x2)
        y = abs(y1 - y2)
        print(x,y)
        i += 1
    # print(absolute)
    file.readline()
    q += 1