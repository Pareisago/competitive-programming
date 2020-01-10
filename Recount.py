import fileinput

file = fileinput.input()

names = []

for line in file:
    line = line.strip()
    if line != '***':
        names.append(line)
    else:
        break

counts = dict()
for i in names:
  counts[i] = counts.get(i, 0) + 1

sorted_d = sorted(counts.items(), key=lambda x: x[1], reverse=True)

if int(sorted_d[0][1]) > int(sorted_d[1][1]):
    print(sorted_d[0][0])
else:
    print('Runoff!')
