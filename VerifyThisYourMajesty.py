import fileinput

set1 = set()
list1 = []
set2 = set()
list2 = []
sum = set()

i = 0
for line in fileinput.input():
    line = line.strip().split()
    if i == 0:
        i += 1
        continue
    else:
        set1.add(line[0])
        list1.append(line[0])
        set2.add(line[1])
        list2.append(line[1])
        sum.add(int(line[0])+int(line[1]))
        i += 1

if len(set1) == len(list1) and len(set2) == len(list2) and len(sum) == len(list1):
    print('CORRECT')
else:
    print('INCORRECT')
# print(set1)
# print(set2)
# print(list1)
# print(list2)
# print(sum)