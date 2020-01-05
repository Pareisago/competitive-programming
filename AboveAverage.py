import fileinput

file = fileinput.input()
count = int(file.readline())

i = 0
while i < count:
    line = file.readline()
    line = line.strip().split()
    students = int(line[0])

    summation = 0
    q = 1
    while q <= students:
        summation += int(line[q])
        q += 1
    average = summation / students

    a = 1
    above_average = 0
    while a <= students:
        if int(line[a]) > average:
            above_average += 1
            a += 1
        else:
            a += 1
    final_num = (above_average/students)*100
    print('{:.3f}%'.format(final_num))
    i += 1