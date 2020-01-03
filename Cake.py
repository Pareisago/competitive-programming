import fileinput

file = fileinput.input()
line = file.readline()
data = line.rstrip().split()
sidetotal = int(data[0])
side1 = int(data[1])
side2 = int(data[2])
diff1 = sidetotal-side1
diff2 = sidetotal-side2

mult1 = 0
mult2 = 0

if side1 > diff1:
    mult1 = side1
else:
    mult1 = diff1

if side2 > diff2:
    mult2 = side2
else:
    mult2 = diff2


def findthebig():
    mult = mult1*mult2*4
    print(mult)


findthebig()
