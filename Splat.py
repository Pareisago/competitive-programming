import fileinput
import math

file = fileinput.input()
tests = int(file.readline())

for i in range(tests):
    drops = int(file.readline())
    biglist = []
    for q in range(drops):
        line = file.readline().split()
        radiussquare = float(line[2])/math.pi
        data = [float(line[0]), float(line[1]), float(radiussquare), line[3]]
        biglist.append(data)
    queries = int(file.readline())
    biglist = biglist[::-1]
    for z in range(queries):
        line = file.readline().split()
        x = float(line[0])
        y = float(line[1])
        ok = False
        for p in biglist:
            xdiff = abs(x-float(p[0]))
            ydiff = abs(y-float(p[1]))
            if xdiff > math.sqrt(p[2]) and ydiff > math.sqrt(p[2]):
                continue
            if xdiff**2 + ydiff**2 < p[2]:
                print(p[3])
                ok = True
                break
        if not ok:
            print('white')