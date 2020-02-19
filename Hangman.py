import fileinput
file = fileinput.input()

word = file.readline()
alpha = file.readline()

i = 0

set = set()

for char in word:
    set.add(char)

set.remove('\n')

for char in alpha:
    if char in set:
        set.remove(char)
        if len(set) == 0:
            print('WIN')
            quit()
    else:
        i += 1
        if i >= 10:
            print('LOSE')
            quit()