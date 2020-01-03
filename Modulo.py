import fileinput
file = fileinput.input()
pset = {'aardvark'}

for i in range(10):
    line = file.readline()
    line = line.strip().split()
    num = int(line[0])
    modulus = int(num) % 42
    pset.add(modulus)

print(len(pset)-1)