import fileinput
import math

file = fileinput.input()

for line in file:
    cur = line.strip().split()
    if cur[0] == '0':
        if cur[1] == '0':
            if cur[2] == '0':
                exit()

    Area_Real = math.pi*(float(cur[0]))**2
    size = int(cur[2]) / int(cur[1])
    square = (2*float(cur[0]))*(2*float(cur[0]))
    size_est = size*square
    print(round(Area_Real, 9), round(size_est, 9))
    # print("{:.9f}".format(Area_Real), "{:.9f}".format(size_est))
