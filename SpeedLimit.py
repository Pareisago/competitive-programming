import fileinput

file = fileinput.input()
line = file.readline()
cases = line[0]
miles = 0
elapsed_time = 0
total = 0
data = line.rstrip().split()
k = 0

while cases != '-1':
    for i in range(int(cases)):
        line = file.readline()
        data = line.rstrip().split()
        miles = int(data[0]) * (int(data[1]) - elapsed_time)
        elapsed_time = int(data[1])
        total = miles + total
    print(str(total) + ' miles')
    total = 0
    elapsed_time = 0
    line = file.readline()
    line = line.rstrip().split()
    cases = line[0]
