import fileinput
from itertools import permutations

file = fileinput.input()
data = int(file.readline())

permutations = [''.join(p) for p in permutations(str(data))]

largest = []
for item in permutations:
    if int(item) > int(data):
        largest.append(item)

largest.sort()
if len(largest) is 0:
    print('0')
else:
    print(largest[0])