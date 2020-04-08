import fileinput

file = fileinput.input()
number = file.readline()

unknowns = file.readline()
unknowns = unknowns.strip().split()

othersounds = set()

for line in file:
    line = line.strip().split()
    if line == ['what', 'does', 'the', 'fox', 'say?']:
        for item in unknowns:
            if item not in othersounds:
                print(item, end=' ')
        print('\n')
        othersounds = set()
        unknowns = file.readline()
        unknowns = unknowns.strip().split()
    else:
        for item in line:
            othersounds.add(item)