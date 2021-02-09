import fileinput
file = fileinput.input()
num = file.readline()[:-1]

while len(num) > 1:
    temp = 1
    
    for c in num:
        c = int(c)
        if c != 0:
            temp *= c
    
    num = str(temp)

print(num)