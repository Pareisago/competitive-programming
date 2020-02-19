import fileinput

file = fileinput.input()
line = file.readline()
line = line.strip().split()

G = int(line[0])
S = int(line[1])
C = int(line[2])

power = 3 * G + 2 * S + C

victory = ''
treasure = ''

if power >= 0:
    treasure = "Copper"

if power >= 2:
    victory = "Estate"

if power >= 3:
    treasure = "Silver"

if power >= 5:
    victory = "Duchy"

if power >= 6:
    treasure = "Gold"

if power >= 8:
    victory = "Province"

if victory == '':
    print(treasure)
    exit()

print(victory + ' or ' + treasure)