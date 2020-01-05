import fileinput

file = fileinput.input()
count = int(file.readline())


def checksum(number):
    summation = 0
    for char in str(number):
        summation += int(char)
    return summation


i = 0
while i < count:
    og_num = int(file.readline())
    og_sum = int(checksum(og_num))
    minus_num = og_num - 1
    while minus_num >= 0:
        if int(checksum(minus_num)) == og_sum - 1:
            print(minus_num)
            break
        else:
            minus_num -= 1
    i += 1
