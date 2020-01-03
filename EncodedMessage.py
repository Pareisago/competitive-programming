import fileinput
from math import sqrt

file = fileinput.input()
line = file.readline()
line = line.strip().split()
Split_Word = []

for i in range(int(line[0])):
    line = file.readline()
    line = line.strip().split()
    word = line[0]
    word_len = len(line[0])
    square = int(sqrt(word_len))

    n = square
    list = [line[0][i:i+n] for i in range(0, len(line[0]), n)]
    string = ''
    q = 0
    while q M< square:
        i = 0
        while i < square:
            string = string + list[i][q]
            i += 1
        q += 1

    list2 = [string[i:i + n] for i in range(0, len(string), n)]

    final = ''
    y = square - 1
    while y >= 0:
        final = final + list2[y]
        y -= 1

    print(final)
