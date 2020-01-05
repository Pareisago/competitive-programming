import fileinput

file = fileinput.input()

count = int(file.readline())
chance_list = []

i = 0
while i < count:
    data = file.readline()
    data = data.strip().split()
    chance_list.append(float(data[1]))
    i += 1

chance_list.sort(reverse=True)

q = 1
summation = 0
for item in chance_list:
    summation += item * q
    q += 1

print(summation)