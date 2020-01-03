import fileinput

file = fileinput.input("test.txt")

line1 = file.readline()
line1 = line1.strip()

line2 = file.readline()
line2 = line2.strip()

line3 = file.readline()
line3 = line3.strip()

print(line1)
print(line2)
print(line3)


def finding(loc):
    if loc ==
# finding location of start
s = 1
if str(s) in line1:
    start = line1.find(str(s))
if str(s) in line2:
    start = line1.find(str(s))
if str(s) in line3:
    start = line1.find(str(s))

i = 2
while i < 10:
    if str(i) in line1:
        loc = line1.find(str(i))
    if str(i) in line2:
        loc = line1.find(str(i))
    if str(i) in line3:
        loc = line1.find(str(i))


