import fileinput

file = fileinput.input('test.txt')

for line in file:
    line = line.strip()
    try:
        num = int(line)
    except Exception:
        string = line

    if string:
        print(num)
        print(string)