import fileinput

line = fileinput.input('test.txt')

line = line.strip().split()
num1 = float(line[0])
num2 = float(line[1])

range = abs(num1-num2) + 1
max = num1 + num2
med = max/2 + 1

i = int(-range/2)
val = 0
while val < range:
    print(med + i)
    i += 1