import fileinput
file = fileinput.input()

i = 0
for line in file:
    line = line.lower()
    if 'rose' in line or 'pink' in line:
        i += 1
    
if i:
    print(i)
else:
    print("I must watch Star Wars with my daughter")
