import fileinput

file = fileinput.input()

starting = int(file.readline())
questions = file.readline()
# Cannot pass 210
total_time = 0
passes = 0

i = 0
while i < int(questions):
    line = file.readline()
    line = line.strip().split()
    total_time = total_time + int(line[0])
    if total_time >= 210:
        break
    if line[1] == 'T':
        passes += 1
    i += 1


final = 0
if starting + passes > 8:
    final = (starting + passes) % 8
else:
    final = starting + passes

print(final)