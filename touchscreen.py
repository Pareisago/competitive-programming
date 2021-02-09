import fileinput

file = fileinput.input("test.txt")

line = file.readline()

l1 = ['q','w','e','r','t','y','u','i','o','p']
l2 = ['a','s','d','f','g','h','j','k','l']
l3 = ['z','x','c','v','b','n','m']

biglist = [l1, l2, l3]
sortlist = []

for line in file:
    line = line.strip().split()
    try:
        count = int(line[1])
        sortlist = []
    except Exception:
        pass
    
    print(line[0])