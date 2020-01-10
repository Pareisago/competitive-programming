import fileinput

file = fileinput.input()
line = file.readline()
line = line.strip().split()

secret = list(line[0])
word = line[1]

for char in word:
    # print('---------')
    # print(secret)
    # print(word)
    # print(char)
    # print('---------')
    if len(secret) == 0:
        print('PASS')
        exit()
    if char == secret[0]:
        secret.remove(secret[0])
    elif char in secret:
        print('FAIL')
        exit()

if len(secret) != 0:
    print('FAIL')
if len(secret) == 0:
    print('PASS')